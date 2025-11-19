# utils/etoile_achat_ventes.py

from graphviz import Digraph


def graphe_etoile_achats_ventes() -> Digraph:
    dot = Digraph("Star_Achats_Ventes_Agreges", format="png", engine="dot")

    dot.attr(
        bgcolor="white",
        fontsize="9",
        rankdir="TB",
        margin="0.1",
        pad="0.1",
    )

    dot.graph_attr.update(
        overlap="false",
        nodesep="0.4",
        ranksep="0.6",
        size="10,6!",
        dpi="120",
    )

    dot.attr("node", fontsize="9", margin="0.08,0.05")
    dot.attr("edge", fontsize="8")

    dot.node(
        "F_ACHATS_VENTES_AGREGES",
        label=(
            "{FAIT_ACHATS_VENTES_AGREGES|"
            "order_item_id\\l"
            "order_id\\l"
            "product_id\\l"
            "seller_id\\l"
            "customer_id\\l"
            "purchase_timestamp\\l"
            "order_status\\l"
            "order_items_count\\l"
            "order_revenue\\l"
            "order_total\\l"
            "order_payment_value\\l"
            "payment_methods_count\\l"
            "payment_installments_max\\l"
            "order_avg_review\\l"
            "order_reviews_count\\l"
            "price\\l"
            "freight_value\\l"
            "line_revenue\\l"
            "line_total\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#eeeeee",
    )

    dot.node(
        "DIM_TEMPS",
        label=(
            "{DIM_TEMPS|"
            "purchase_timestamp\\l"
            "order_purchase_timestamp\\l"
            "annee\\l"
            "trimestre\\l"
            "mois\\l"
            "jour\\l"
            "semaine\\l"
            "annee_semaine\\l"
            "annee_mois\\l"
            "annee_trimestre\\l"
            "annee_jour\\l"
            "heure\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#d0e6ff",
    )

    dot.node(
        "DIM_PRODUIT",
        label=(
            "{DIM_PRODUIT|"
            "product_id\\l"
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
        fillcolor="#f0d9ff",
    )

    dot.node(
        "DIM_VENDEUR",
        label=(
            "{DIM_VENDEUR|"
            "seller_id\\l"
            "zip_code\\l"
            "city\\l"
            "state\\l"
            "name_state\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffe6c9",
    )

    dot.node(
        "DIM_CLIENT",
        label=(
            "{DIM_CLIENT|"
            "customer_id\\l"
            "zip_code\\l"
            "city\\l"
            "state\\l"
            "name_state\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#d0ffd6",
    )

    dot.node(
        "DIM_GEOLOCALISATION",
        label=(
            "{DIM_GEOLOCALISATION|"
            "zip_code\\l"
            "city_geo\\l"
            "state_geo\\l"
            "lat_min\\l"
            "lat\\l"
            "lat_max\\l"
            "lng_min\\l"
            "lng\\l"
            "lng_max\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffd9df",
    )

    dot.node(
        "DIM_STATUT",
        label=(
            "{DIM_STATUT_COMMANDE|"
            "order_status\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffffcc",
    )

    dot.node(
        "DIM_PAIEMENT",
        label=(
            "{DIM_PAIEMENT|"
            "order_id\\l"
            "payment_main_type\\l"
            "payment_methods_count\\l"
            "payment_installments_max\\l"
            "payment_types_concat\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#e0fff5",
    )

    dot.edge(
        "F_ACHATS_VENTES_AGREGES",
        "DIM_TEMPS",
        label="purchase_timestamp / order_purchase_timestamp",
    )
    dot.edge(
        "F_ACHATS_VENTES_AGREGES",
        "DIM_PRODUIT",
        label="product_id",
    )
    dot.edge(
        "F_ACHATS_VENTES_AGREGES",
        "DIM_VENDEUR",
        label="seller_id",
    )
    dot.edge(
        "F_ACHATS_VENTES_AGREGES",
        "DIM_CLIENT",
        label="customer_id",
    )
    dot.edge(
        "F_ACHATS_VENTES_AGREGES",
        "DIM_STATUT",
        label="order_status",
    )
    dot.edge(
        "F_ACHATS_VENTES_AGREGES",
        "DIM_PAIEMENT",
        label="order_id",
    )

    dot.edge(
        "DIM_CLIENT",
        "DIM_GEOLOCALISATION",
        label="zip_code",
        style="dashed",
    )
    dot.edge(
        "DIM_VENDEUR",
        "DIM_GEOLOCALISATION",
        label="zip_code",
        style="dashed",
    )

    return dot