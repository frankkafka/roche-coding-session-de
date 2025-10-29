# Snakefile

# -------------  FINAL TARGET -------------
rule all:
    input:
        "data/processed/analytics.sqlite"


# -------------  MAIN RULE -------------
rule build_sqlite:
    input:
        users="data/raw/users.csv",
        orders="data/raw/orders.csv"
    output:
        db="data/processed/analytics.sqlite"
    shell:
        """
        python scripts/process_data.py \
            --users_csv {input.users} \
            --orders_csv {input.orders} \
            --output_db {output.db}
        """
