# utils/etoile_ventes_avis.py

from graphviz import Digraph


def graphe_etoile_ventes_avis() -> Digraph:
    dot_ventes = Digraph("Star_Ventes_Avis", format="png", engine="dot")
    dot_ventes.attr(bgcolor="white", fontsize="10")

    dot_ventes.graph_attr.update(
        overlap="false",
        nodesep="0.6",
        ranksep="0.9"
    )

    dot_ventes.node(
        "F_VENTES_AVIS",
        label=(
            "{FAIT_VENTES_AVIS|"
            "order_id\\l"
            "customer_id\\l"
            "zip_code\\l"
            "purchase_timestamp\\l"
            "order_status\\l"
            "value\\l"
            "value_*\\l"
            "int_*\\l"
            "score\\l"
            "score_1..5\\l"
            "approuvee\\l"
            "envoyee\\l"
            "livree\\l"
            "estimee\\l"
            "creation\\l"
            "answer\\l"
            "comment_length\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#eeeeee"
    )

    dot_ventes.node(
        "DIM_TEMPS",
        label=(
            "{DIM_TEMPS|"
            "purchase_timestamp\\l"
            "annee\\l"
            "trimestre\\l"
            "mois\\l"
            "jour\\l"
            "semaine\\l"
            "annee_mois\\l"
            "annee_trimestre\\l"
            "annee_jour\\l"
            "heure\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#d0e6ff"
    )

    dot_ventes.node(
        "DIM_CLIENT",
        label=(
            "{DIM_CLIENT|"
            "customer_id\\l"
            "city\\l"
            "state\\l"
            "name_state\\l"
            "zip_code\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#d0ffd6"
    )

    dot_ventes.node(
        "DIM_GEOCLIENT",
        label=(
            "{DIM_GEOLOCALISATION_CLIENT|"
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
        fillcolor="#ffe6c9"
    )

    dot_ventes.node(
        "DIM_PAIEMENT",
        label=(
            "{DIM_PAIEMENT|"
            "order_id\\l"
            "int_credit_card\\l"
            "int_boleto\\l"
            "value_credit_card\\l"
            "value_boleto\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#f0d9ff"
    )

    dot_ventes.node(
        "DIM_AVIS",
        label=(
            "{DIM_AVIS|"
            "order_id\\l"
            "score_1..5\\l"
            "creation_1..5\\l"
            "answer_1..5\\l"
            "comment_1..5\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffd9df"
    )

    dot_ventes.node(
        "DIM_STATUT",
        label=(
            "{DIM_STATUT_COMMANDE|"
            "order_status\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffffcc"
    )

    dot_ventes.edge("F_VENTES_AVIS", "DIM_TEMPS",     label="purchase_timestamp", fontsize="9")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_CLIENT",    label="customer_id",        fontsize="9")
    dot_ventes.edge("DIM_CLIENT",    "DIM_GEOCLIENT", label="zip_code",           fontsize="9", style="dashed")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_PAIEMENT",  label="order_id",           fontsize="9")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_AVIS",      label="order_id",           fontsize="9")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_STATUT",    label="order_status",       fontsize="9")

    return dot_ventes
