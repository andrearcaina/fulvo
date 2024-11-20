from .house_league_controller import list_all_hl, list_hl_by_id, create_hl, update_hl, delete_hl
from .match_stats_controller import list_all_ms, list_ms_by_id, create_ms, update_ms, delete_ms
from .match_referee_controller import list_all_mr, list_mr_by_id, create_mr, update_mr, delete_mr
from .player_controller import list_all_ps, list_ps_by_id, update_ps, delete_ps
from .referee_controller import list_all_rs, list_rs_by_id, update_rs, delete_rs
from .team_controller import list_all_ts, list_ts_by_id, create_ts, update_ts, delete_ts
from .user_controller import list_all_us, list_us_by_id, create_us, update_us, delete_us
from .menu_controller import drop_db, create_db, populate_db, queries_db

# functions to query all records in a table
__all__ = ["list_all_hl", "list_all_ms", "list_all_mr", "list_all_ps", "list_all_rs", "list_all_ts", "list_all_us"]
# functions to query a record by id
__all__ += ["list_hl_by_id", "list_ms_by_id", "list_mr_by_id", "list_ps_by_id", "list_rs_by_id", "list_ts_by_id", "list_us_by_id"]
# functions to create a record
__all__ += ["create_us", "create_ts", "create_hl", "create_mr", "create_ms"]
# function to update a record
__all__ += ["update_us", "update_ps", "update_rs", "update_ts", "update_hl", "update_mr", "update_ms"]
# function to delete a record
__all__ += ["delete_us", "delete_ps", "delete_rs", "delete_ts", "delete_hl", "delete_mr", "delete_ms"]
# functions to drop, create, populate the database
__all__ += ["drop_db", "create_db", "populate_db", "queries_db"]