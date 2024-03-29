import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Customizable graphics for each country", href="/page-1")),
        dbc.NavItem(dbc.NavLink("Covid Factor", href="/page-2")),
        dbc.NavItem(dbc.NavLink("Selected countries (grouped)", href="/page-3")),
    ],
    brand="Analysis of economic data based on COVID-10 data | 2019 - 2023",
    brand_href="/",
    color="primary",
    dark=True,
)
