# utils/etoile_achat_ventes.py

from graphviz import Digraph


def graphe_etoile_achats_ventes() -> Digraph:
    """
    Génère le schéma en étoile de la table de faits :
    FAIT_ACHATS_VENTES_AGREGES (grain = order_item_id).
    """
    dot = Digraph("Star_Achats_Ventes_Agreges", format="png", engine="dot")

    # Attributs globaux du graphe
    dot.attr(
        bgcolor="white",
        fontsize="9",
        rankdir="TB",   # top -> bottom
        margin="0.1",
        pad="0.1",
    )

    dot.graph_attr.update(
        overlap="false",
        nodesep="0.4",
        ranksep="0.6",
        size="10,6!",   # taille cible (pouces) pour le rendu PNG
        dpi="120",
    )

    # Attributs globaux des noeuds / arêtes
    dot.attr("node", fontsize="9", margin="0.08,0.05")
    dot.attr("edge", fontsize="8")

    # ------------------------------------------------------------------
    # TABLE DE FAITS
    # ------------------------------------------------------------------
    dot.node(
        "F_ACHATS_VENTES_AGREGES",
        label=(
            "{FAIT_ACHATS_VENTES_AGREGES|"
            "grain: order_item_id (ligne de commande)\\l"
            "---------------------\\l"
            "Clés : order_item_id, order_id, product_id, seller_id, customer_id\\l"
            "       purchase_timestamp, order_status, order_id (FK DIM_PAIEMENT)\\l"
            "---------------------\\l"
            "Mesures ligne (items) : price, freight_value, line_revenue, line_total\\l"
            "Mesures agrégées commande : order_items_count, order_revenue, order_total, ...\\l"
            "Paiement (agrégé) : order_payment_value, payment_methods_count, ...\\l"
            "Avis (agrégé, optionnel) : order_avg_review, order_reviews_count\\l"
            "}"
        ),
        shape="record",
        style="filled",
        fillcolor="#eeeeee",
)


    # ------------------------------------------------------------------
    # DIMENSIONS
    # ------------------------------------------------------------------
    dot.node(
        "DIM_TEMPS",
        label=(
            "{DIM_TEMPS|"
            "+ purchase_timestamp / order_purchase_timestamp (PK)\\l"
            "---------------------\\l"
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
        fillcolor="#f0d9ff",
    )

    dot.node(
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
        fillcolor="#ffe6c9",
    )

    dot.node(
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
        fillcolor="#d0ffd6",
    )

    dot.node(
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
        fillcolor="#ffd9df",
    )

    dot.node(
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
        fillcolor="#ffffcc",
    )

    dot.node(
        "DIM_PAIEMENT",
        label=(
            "{DIM_PAIEMENT|"
            "+ order_id (PK)\\l"
            "---------------------\\l"
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

    # ------------------------------------------------------------------
    # ARÊTES (RELATIONS)
    # ------------------------------------------------------------------
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
        label="order_id (profil paiement agrégé)",
    )

    # Liens géographiques (clients / vendeurs -> géolocalisation)
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


if __name__ == "__main__":
    # Génération directe du PNG si le script est exécuté seul
    g = graphe_etoile_achats_ventes()
    g.render("Star_Achats_Ventes_Agreges", cleanup=True)
