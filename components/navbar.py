import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Economic Factor", href="/page-1")),
        dbc.NavItem(dbc.NavLink("Covid Factor", href="/page-2")),
        dbc.NavItem(dbc.NavLink("Selected countries", href="/page-3")),
    ],
    brand="My first DashBoard",
    brand_href="/",
    color="primary",
    dark=True,
)
