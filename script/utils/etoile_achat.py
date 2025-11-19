# utils/etoile_achat.py

from graphviz import Digraph


def graphe_etoile_achat() -> Digraph:
    dot_achats = Digraph("Star_Achats", format="png", engine="dot")
    dot_achats.attr(bgcolor="white", fontsize="10")

    dot_achats.graph_attr.update(
        overlap="false",
        nodesep="0.6",
        ranksep="0.9"
    )

    dot_achats.node(
        "F_ACHATS",
        label=(
            "{FAIT_ACHATS|"
            "grain: order_item_id\\l"
            "---------------------\\l"
            "+ order_item_id\\l"
            "+ order_id\\l"
            "+ product_id\\l"
            "+ seller_id\\l"
            "+ customer_id\\l"
            "+ zip_code\\l"
            "+ purchase_timestamp\\l"
            "+ order_status\\l"
            "---------------------\\l"
            "Mesures principales:\\l"
            "- price\\l"
            "- freight_value\\l"
            "- line_revenue\\l"
            "- line_total\\l"
            "- limit (h, shipping_limit - purchase)\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#eeeeee"
    )

    dot_achats.node(
        "DIM_TEMPS",
        label=(
            "{DIM_TEMPS|"
            "+ purchase_timestamp (PK)\\l"
            "---------------------\\l"
            "annee\\l"
            "trimestre\\l"
            "mois\\l"
            "jour\\l"
            "semaine\\l"
            "annee_semaine\\l"
            "annee_mois\\l"
            "heure\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#d0e6ff"
    )

    dot_achats.node(
        "DIM_PRODUIT",
        label=(
            "{DIM_PRODUIT|"
            "+ product_id (PK)\\l"
            "---------------------\\l"
            "category_name\\l"
            "name_lenght\\l"
            "description_lenght\\l"
            "photos_qty\\l"
            "weight_g\\l"
            "length_cm\\l"
            "height_cm\\l"
            "width_cm\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#f0d9ff"
    )

    dot_achats.node(
        "DIM_VENDEUR",
        label=(
            "{DIM_VENDEUR|"
            "+ seller_id (PK)\\l"
            "---------------------\\l"
            "zip_code (FK geo)\\l"
            "city\\l"
            "state (sigle)\\l"
            "name_state\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffe6c9"
    )

    dot_achats.node(
        "DIM_CLIENT",
        label=(
            "{DIM_CLIENT|"
            "+ customer_id (PK)\\l"
            "---------------------\\l"
            "zip_code (FK geo)\\l"
            "city\\l"
            "state (sigle)\\l"
            "name_state\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#d0ffd6"
    )

    dot_achats.node(
        "DIM_GEOLOCALISATION",
        label=(
            "{DIM_GEOLOCALISATION|"
            "+ zip_code (PK)\\l"
            "---------------------\\l"
            "city_geo\\l"
            "state_geo\\l"
            "lat_min, lat, lat_max\\l"
            "lng_min, lng, lng_max\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffd9df"
    )

    dot_achats.node(
        "DIM_STATUT",
        label=(
            "{DIM_STATUT_COMMANDE|"
            "+ order_status (PK)\\l"
            "---------------------\\l"
            "ex: delivered, shipped, canceled, ...\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffffcc"
    )

    dot_achats.edge("F_ACHATS", "DIM_TEMPS",          label="purchase_timestamp", fontsize="9")
    dot_achats.edge("F_ACHATS", "DIM_PRODUIT",        label="product_id",         fontsize="9")
    dot_achats.edge("F_ACHATS", "DIM_VENDEUR",        label="seller_id",          fontsize="9")
    dot_achats.edge("F_ACHATS", "DIM_CLIENT",         label="customer_id",        fontsize="9")
    dot_achats.edge("F_ACHATS", "DIM_STATUT",         label="order_status",       fontsize="9")

    dot_achats.edge("DIM_CLIENT",  "DIM_GEOLOCALISATION", label="zip_code", fontsize="9", style="dashed")
    dot_achats.edge("DIM_VENDEUR", "DIM_GEOLOCALISATION", label="zip_code", fontsize="9", style="dashed")

    return dot_achats
