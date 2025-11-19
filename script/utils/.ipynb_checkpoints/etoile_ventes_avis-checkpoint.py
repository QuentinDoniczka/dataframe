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

    # ========= 1. Table de faits =========
    dot_ventes.node(
        "F_VENTES_AVIS",
        label=(
            "{FAIT_VENTES_AVIS|"
            "grain: order_id\\l"
            "---------------------\\l"
            "+ order_id\\l"
            "+ customer_id\\l"
            "+ zip_code\\l"
            "+ purchase_timestamp\\l"
            "+ order_status\\l"
            "---------------------\\l"
            "Mesures principales:\\l"
            "- value (total payé)\\l"
            "- value_* par type paiement\\l"
            "- int_* (installments)\\l"
            "- score, score_1..5\\l"
            "- approuvee, envoyee, livree, estimee (h)\\l"
            "- creation, answer (h)\\l"
            "- comment (longueur totale)\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#eeeeee"
    )

    # ========= 2. Dimensions =========
    dot_ventes.node(
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
            "+ customer_id (PK)\\l"
            "---------------------\\l"
            "city\\l"
            "state (sigle)\\l"
            "name_state\\l"
            "zip_code (FK geo)\\l"
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
        fillcolor="#ffe6c9"
    )

    dot_ventes.node(
        "DIM_PAIEMENT",
        label=(
            "{DIM_PAIEMENT|"
            "+ order_id (PK)\\l"
            "---------------------\\l"
            "int_credit_card, int_boleto, ...\\l"
            "value_credit_card, value_boleto, ...\\l"
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
            "+ order_id (PK)\\l"
            "---------------------\\l"
            "score_1..5\\l"
            "creation_1..5 (h)\\l"
            "answer_1..5 (h)\\l"
            "comment_1..5 (len)\\l"
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
            "+ order_status (PK)\\l"
            "---------------------\\l"
            "ex: delivered, shipped, canceled, ...\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#ffffcc"
    )

    # ========= 3. Arêtes =========
    dot_ventes.edge("F_VENTES_AVIS", "DIM_TEMPS",      label="purchase_timestamp", fontsize="9")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_CLIENT",     label="customer_id",        fontsize="9")
    dot_ventes.edge("DIM_CLIENT",    "DIM_GEOCLIENT",  label="zip_code",           fontsize="9", style="dashed")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_PAIEMENT",   label="order_id",           fontsize="9")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_AVIS",       label="order_id",           fontsize="9")
    dot_ventes.edge("F_VENTES_AVIS", "DIM_STATUT",     label="order_status",       fontsize="9")

    return dot_ventes
