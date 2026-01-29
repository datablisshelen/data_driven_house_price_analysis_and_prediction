import streamlit as st

st.set_page_config(page_title="House Price Analytics", layout="wide")
st.title("House Price Analytics & Prediction")
import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="House Price Analysis",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 Data-driven House Price Analysis")
st.write("Target variable: **Saleprice**")


# -----------------------------
# Load data 
# -----------------------------
@st.cache_data
def load_csv(path: str) -> pd.DataFrame:
    df_ = pd.read_csv(path)
    return df_


DATA_PATH = "../data/raw/Cleaned train.csv"


try:
    df = load_csv(DATA_PATH)
except FileNotFoundError:
    st.error(
        "File not found. Check the path to the dataset.\n\n"
        f"Current path: `{DATA_PATH}`"
    )
    st.stop()

if "Saleprice" not in df.columns:
    st.error("Column `Saleprice` was not found in this file.")
    st.stop()


# -----------------------------
# Restore Neighborhood 
# -----------------------------
def restore_neighborhood(dataframe: pd.DataFrame) -> pd.DataFrame:
    nb_cols = [c for c in dataframe.columns if c.startswith("Neighborhood_")]

    if not nb_cols:
        dataframe["Neighborhood"] = "Unknown"
        return dataframe

    dataframe["Neighborhood"] = (
        dataframe[nb_cols]
        .idxmax(axis=1)
        .str.replace("Neighborhood_", "", regex=False)
    )
    return dataframe


df = restore_neighborhood(df)


# -----------------------------
# Sidebar filters 
# -----------------------------
st.sidebar.header("Filters")

year_col = "YearBuilt"
area_col = "GrLivArea"
qual_col = "OverallQual"

# Year filter
if year_col in df.columns:
    year_min = int(df[year_col].min())
    year_max = int(df[year_col].max())
    year_default = (
        int(df[year_col].quantile(0.10)),
        int(df[year_col].quantile(0.90)),
    )

    year_range = st.sidebar.slider(
        "Year Built",
        year_min,
        year_max,
        year_default,
    )
else:
    year_range = None
    st.sidebar.warning("YearBuilt not found — year filter disabled.")

# Quality filter
if qual_col in df.columns:
    qual_options = sorted(df[qual_col].dropna().unique())
    qual_selected = st.sidebar.multiselect(
        "Overall Quality",
        options=qual_options,
        default=qual_options,
    )
else:
    qual_selected = None
    st.sidebar.warning("OverallQual not found — quality filter disabled.")

# Area filter
if area_col in df.columns:
    a_min = int(df[area_col].min())
    a_max = int(df[area_col].max())
    a_default = (
        int(df[area_col].quantile(0.10)),
        int(df[area_col].quantile(0.90)),
    )

    area_range = st.sidebar.slider(
        "Living Area (GrLivArea)",
        a_min,
        a_max,
        a_default,
    )
else:
    area_range = None
    st.sidebar.warning("GrLivArea not found — area filter disabled.")

# Neighborhood filter
if "Neighborhood" in df.columns:
    nb_list = sorted(df["Neighborhood"].dropna().unique())
    nb_selected = st.sidebar.multiselect(
        "Neighborhood",
        options=nb_list,
        default=[],
    )
else:
    nb_selected = None


# Apply filters
df_f = df.copy()

if year_range and year_col in df_f.columns:
    df_f = df_f[df_f[year_col].between(year_range[0], year_range[1])]

if qual_selected is not None and qual_col in df_f.columns:
    df_f = df_f[df_f[qual_col].isin(qual_selected)]

if area_range and area_col in df_f.columns:
    df_f = df_f[df_f[area_col].between(area_range[0], area_range[1])]

if nb_selected:
    df_f = df_f[df_f["Neighborhood"].isin(nb_selected)]

if df_f.empty:
    st.warning("No rows match current filters. Try widening filters.")
    st.stop()


# -----------------------------
# Tabs 
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview", "Visuals", "Drivers", "Data"]
)


# =============================
# TAB 1 — Overview
# =============================
with tab1:
    st.subheader("Overview")

    c1, c2, c3 = st.columns(3)
    c1.metric("Rows (filtered)", len(df_f))
    c2.metric("Median Saleprice", f"{df_f['Saleprice'].median():.0f}")

    if area_col in df_f.columns:
        c3.metric("Median GrLivArea", f"{df_f[area_col].median():.0f}")
    else:
        c3.metric("Median GrLivArea", "n/a")

    st.markdown("### AI-generated insight summary")
    st.caption("AI-assisted draft summary. Please validate using the charts.")

    num_cols = df_f.select_dtypes(include="number").columns.tolist()
    summary = "Not enough numeric columns to calculate relationships."

    if len(num_cols) > 3:
        corr = (
            df_f[num_cols]
            .corr(numeric_only=True)["Saleprice"]
            .sort_values(ascending=False)
        )
        top_feats = corr.index[1:6].tolist()

        summary = (
            f"For the current filters (n={len(df_f)}), median Saleprice is "
            f"{df_f['Saleprice'].median():.0f}. "
            f"Top positively related numeric features here are: "
            f"{', '.join(top_feats)}. "
            "This is correlation-based, not causation."
        )

    st.info(summary)


# =============================
# TAB 2 — Visuals (4+ plot types)
# =============================
with tab2:
    st.subheader("Visualisations")

    st.markdown("**Saleprice distribution**")
    fig_hist = px.histogram(
        df_f,
        x="Saleprice",
        nbins=30,
        title="Saleprice Distribution (filtered)",
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    if area_col in df_f.columns and qual_col in df_f.columns:
        st.markdown("**Living area vs Saleprice**")
        fig_scatter = px.scatter(
            df_f,
            x=area_col,
            y="Saleprice",
            color=qual_col,
            hover_data=[year_col] if year_col in df_f.columns else None,
            title="GrLivArea vs Saleprice (color = OverallQual)",
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    if qual_col in df_f.columns:
        st.markdown("**Saleprice by OverallQual**")
        fig_box = px.box(
            df_f,
            x=qual_col,
            y="Saleprice",
            title="Saleprice by OverallQual",
        )
        st.plotly_chart(fig_box, use_container_width=True)

    if "Neighborhood" in df_f.columns:
        st.markdown("**Neighborhood comparison (median Saleprice)**")

        top_n = st.slider(
            "Top N neighborhoods",
            min_value=5,
            max_value=25,
            value=12,
        )

        nb_med = (
            df_f.groupby("Neighborhood", as_index=False)["Saleprice"]
            .median()
            .sort_values("Saleprice", ascending=False)
            .head(top_n)
        )

        fig_nb = px.bar(
            nb_med,
            x="Neighborhood",
            y="Saleprice",
            title=f"Top {top_n} Neighborhoods by Median Saleprice",
        )
        st.plotly_chart(fig_nb, use_container_width=True)


# =============================
# TAB 3 — Drivers (simple correlation view)
# =============================
with tab3:
    st.subheader("Drivers (simple view)")

    numeric_cols = df_f.select_dtypes(include="number").columns.tolist()

    if "Saleprice" not in numeric_cols:
        st.warning("Saleprice is not numeric in this dataset.")
        st.stop()

    if len(numeric_cols) < 5:
        st.warning("Not enough numeric columns for driver analysis.")
        st.stop()

    corr_series = (
        df_f[numeric_cols]
        .corr(numeric_only=True)["Saleprice"]
        .dropna()
        .sort_values(ascending=False)
    )

    corr_series = corr_series.drop(index="Saleprice", errors="ignore")

    top_k = st.slider(
        "How many drivers to show?",
        min_value=5,
        max_value=20,
        value=10,
    )

    corr_top = corr_series.head(top_k).reset_index()
    corr_top.columns = ["Feature", "Correlation"]

    fig_drivers = px.bar(
        corr_top,
        x="Correlation",
        y="Feature",
        orientation="h",
        title="Top numeric correlations with Saleprice (filtered)",
    )
    st.plotly_chart(fig_drivers, use_container_width=True)

    show_heatmap = st.checkbox("Show correlation heatmap (top 12 features)")
    if show_heatmap:
        keep_cols = ["Saleprice"] + corr_series.head(11).index.tolist()
        heat = df_f[keep_cols].corr(numeric_only=True)

        fig_heat = px.imshow(
            heat,
            title="Correlation heatmap (selected features)",
        )
        st.plotly_chart(fig_heat, use_container_width=True)


# =============================
# TAB 4 — Data
# =============================
with tab4:
    st.subheader("Data preview")

    st.write("First 50 rows of the filtered dataset:")
    st.dataframe(df_f.head(50))

  
    csv_bytes = df_f.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download filtered data (CSV)",
        data=csv_bytes,
        file_name="filtered_train.csv",
        mime="text/csv",
    )
