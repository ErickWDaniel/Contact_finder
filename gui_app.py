#!/usr/bin/env python3
"""Simple Tkinter GUI for Tanzania contact finder."""

import importlib.util
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox


def _load_contact_finder():
    module_path = Path(__file__).resolve().parent / "contact-inder_enhanced.py"
    spec = importlib.util.spec_from_file_location("contact_finder_app", module_path)
    module = importlib.util.module_from_spec(spec)
    if spec and spec.loader:
        spec.loader.exec_module(module)
    return module.TanzaniaContactFinder


SERVICE_OPTIONS = [
    ("tanzapages", "Tanzapages Directory ⚡"),
    ("schoolcotz", "School.co.tz (O-level Schools) ⚡"),
    ("zoomtanzania", "ZoomTanzania Directory ⚡"),
    ("yellowpages", "TZ Yellow Pages"),
    ("google_maps", "Google Maps"),
    ("education_portal", "Education Portals"),
    ("shulezetu", "Shulezetu Directory"),
    ("facebook", "Facebook Pages"),
    ("brela", "BRELA Registry")
]

ORG_TYPES = [
    ("school", "School"),
    ("business", "Business"),
    ("medical", "Medical"),
    ("restaurant", "Restaurant"),
    ("retail", "Retail"),
    ("service", "Service"),
    ("nonprofit", "Nonprofit")
]

REGIONS = [
    "All Tanzania Regions",
    "Arusha", "Dar es Salaam", "Dodoma", "Geita", "Iringa", "Kagera",
    "Katavi", "Kigoma", "Kilimanjaro", "Lindi", "Manyara", "Mara",
    "Mbeya", "Morogoro", "Mtwara", "Mwanza", "Njombe", "Pemba North",
    "Pemba South", "Pwani", "Rukwa", "Ruvuma", "Shinyanga", "Simiyu",
    "Singida", "Songwe", "Tabora", "Tanga", "Zanzibar Central/South",
    "Zanzibar North", "Zanzibar Urban/West"
]


class ContactFinderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tanzania Contact Finder")
        self.geometry("720x760")
        self.minsize(640, 680)
        self.resizable(True, True)

        self.org_type = tk.StringVar(value="school")
        self.location = tk.StringVar(value="All Tanzania Regions")
        self.keywords = tk.StringVar(value="")
        self.limit = tk.StringVar(value="100")
        self.output = tk.StringVar(value="results.csv")
        self.verify_websites = tk.BooleanVar(value=True)
        self.pdf_urls = tk.StringVar(value="")
        self.services = {key: tk.BooleanVar(value=False) for key, _ in SERVICE_OPTIONS}

        self._build_form()

    def _build_form(self):
        frame = tk.Frame(self, padx=16, pady=16)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Organization Type", font=("Arial", 10, "bold")).pack(anchor="w")
        type_menu = tk.OptionMenu(frame, self.org_type, *[key for key, _ in ORG_TYPES])
        type_menu.pack(fill=tk.X, pady=(4, 10))

        tk.Label(frame, text="Location", font=("Arial", 10, "bold")).pack(anchor="w")
        location_menu = tk.OptionMenu(frame, self.location, *REGIONS)
        location_menu.pack(fill=tk.X, pady=(4, 10))

        tk.Label(frame, text="Keywords (comma-separated)", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Entry(frame, textvariable=self.keywords).pack(fill=tk.X, pady=(4, 10))

        tk.Label(frame, text="Max Results", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Entry(frame, textvariable=self.limit).pack(fill=tk.X, pady=(4, 10))

        tk.Label(frame, text="Output CSV filename", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Entry(frame, textvariable=self.output).pack(fill=tk.X, pady=(4, 10))

        tk.Label(frame, text="Sources", font=("Arial", 10, "bold")).pack(anchor="w")
        sources_frame = tk.Frame(frame)
        sources_frame.pack(fill=tk.X, pady=(4, 10))
        columns = 2
        for idx, (key, label) in enumerate(SERVICE_OPTIONS):
            row = idx // columns
            col = idx % columns
            tk.Checkbutton(
                sources_frame,
                text=label,
                variable=self.services[key],
                onvalue=True,
                offvalue=False
            ).grid(row=row, column=col, sticky="w", padx=6, pady=2)

        tk.Label(frame, text="If no sources are selected, all sources are used.", fg="#666").pack(anchor="w")

        tk.Checkbutton(
            frame,
            text="Verify websites via DuckDuckGo",
            variable=self.verify_websites,
            onvalue=True,
            offvalue=False
        ).pack(anchor="w", pady=(10, 4))

        tk.Label(frame, text="PDF URLs (one per line)", font=("Arial", 10, "bold")).pack(anchor="w")
        pdf_box = tk.Text(frame, height=4)
        pdf_box.pack(fill=tk.X, pady=(4, 10))
        self.pdf_box = pdf_box

        self.status = tk.StringVar(value="Ready")
        tk.Label(frame, textvariable=self.status, fg="#444").pack(anchor="w", pady=(4, 0))

        self.run_button = tk.Button(frame, text="Run Search", command=self.run_search, bg="#0a6", fg="#fff")
        self.run_button.pack(fill=tk.X, pady=(16, 0))

    def run_search(self):
        try:
            limit_value = int(self.limit.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Max Results must be a number.")
            return

        selected_services = [key for key, var in self.services.items() if var.get()]
        keywords = [item.strip() for item in self.keywords.get().split(",") if item.strip()]
        pdf_urls = [line.strip() for line in self.pdf_box.get("1.0", tk.END).splitlines() if line.strip()]

        self.run_button.config(state=tk.DISABLED)
        self.status.set("Searching... this may take a few minutes")

        def _worker():
            try:
                TanzaniaContactFinder = _load_contact_finder()
                finder = TanzaniaContactFinder()
                finder.config["verify_websites"] = bool(self.verify_websites.get())
                if pdf_urls:
                    finder.config["pdf_urls"] = pdf_urls

                location_value = self.location.get().strip()
                if location_value == "All Tanzania Regions":
                    locations = [region for region in REGIONS if region != "All Tanzania Regions"]
                    locations = [f"{region}, Tanzania" for region in locations]
                    finder.search_across_locations(
                        org_type=self.org_type.get().strip(),
                        locations=locations,
                        keywords=keywords,
                        limit=limit_value,
                        service=selected_services or "all"
                    )
                else:
                    finder.search_online_sources(
                        org_type=self.org_type.get().strip(),
                        location=location_value,
                        keywords=keywords,
                        limit=limit_value,
                        service=selected_services or "all"
                    )

                output_file = self.output.get().strip() or "results.csv"
                finder.save_csv(output_file)

                self._notify_success(output_file, finder.stats['total'])
            except Exception as exc:
                self._notify_error(str(exc))
            finally:
                self._reset_ui()

        threading.Thread(target=_worker, daemon=True).start()

    def _notify_success(self, output_file: str, total: int):
        def _show():
            if not self.winfo_exists():
                return
            self.status.set("Done")
            messagebox.showinfo(
                "Search Complete",
                f"Saved results to {output_file}.\nTotal found: {total}"
            )

        self.after(0, _show)

    def _notify_error(self, message: str):
        def _show():
            if not self.winfo_exists():
                return
            self.status.set("Failed")
            messagebox.showerror("Search Failed", message)

        self.after(0, _show)

    def _reset_ui(self):
        def _reset():
            if not self.winfo_exists():
                return
            self.run_button.config(state=tk.NORMAL)

        self.after(0, _reset)


def main() -> None:
    app = ContactFinderApp()
    app.mainloop()


if __name__ == "__main__":
    main()
