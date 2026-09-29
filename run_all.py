from src.config import load_config

def main():
    cfg = load_config()
    print("Config loaded. Reporting date:", cfg["project"]["reporting_date"])
    # Part 2: build_data(cfg)
    # Part 3: run_baseline(cfg)
    # Part 4: run_climate(cfg)
    # Part 5: run_critical_tests(cfg)

if __name__ == "__main__":
    main()
