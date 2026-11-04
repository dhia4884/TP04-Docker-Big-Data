
import csv
import os
from collections import Counter

DATA_FILE = "/app/data/air_quality_5gb.csv"
CHUNK_SIZE = 100_000


def analyze_data():
    if not os.path.isfile(DATA_FILE):
        print(f"ERROR: Dataset not found: {DATA_FILE}")
        print("Check that the dataset is mounted into the container.")
        return

    file_size = os.path.getsize(DATA_FILE)
    print("=" * 50)
    print("AIR QUALITY DATASET ANALYSIS")
    print("=" * 50)
    print(f"File size: {file_size / (1024 ** 3):.2f} GiB")
    print(f"Chunk size: {CHUNK_SIZE:,} rows")

    total_rows = 0
    district_counts = Counter()
    temperature_sum = 0.0
    temperature_count = 0
    aqi_sum = 0.0
    aqi_count = 0

    with open(DATA_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_rows += 1

            district = row.get("district", "").strip()
            if district:
                district_counts[district] += 1

            temperature = row.get("temperature_c", "").strip()
            if temperature:
                try:
                    temperature_sum += float(temperature)
                    temperature_count += 1
                except ValueError:
                    pass

            aqi = row.get("air_quality_index", "").strip()
            if aqi:
                try:
                    aqi_sum += float(aqi)
                    aqi_count += 1
                except ValueError:
                    pass

            if total_rows % CHUNK_SIZE == 0:
                print(f"Processed {total_rows:,} rows...")

    print("\nANALYSIS RESULTS")
    print("-" * 50)
    print(f"Total data rows: {total_rows:,}")

    print("\nRows by district:")
    for district, count in district_counts.most_common():
        print(f"  {district}: {count:,}")

    if temperature_count:
        print(f"\nAverage temperature: {temperature_sum / temperature_count:.2f} °C")

    if aqi_count:
        print(f"Average air quality index: {aqi_sum / aqi_count:.2f}")

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    analyze_data()
