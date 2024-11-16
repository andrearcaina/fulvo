from .house_league_controller import list_all_hl, list_hl_by_id
from .match_stats_controller import list_all_ms, list_ms_by_id
from .match_referee_controller import list_all_mr, list_mr_by_id
from .player_controller import list_all_ps, list_ps_by_id, update_ps, delete_ps
from .referee_controller import list_all_rs, list_rs_by_id, update_rs, delete_rs
from .team_controller import list_all_ts, list_ts_by_id
from .user_controller import list_all_us, list_us_by_id, create_us, update_us, delete_us

# functions to query all records in a table
__all__ = ["list_all_hl", "list_all_ms", "list_all_mr", "list_all_ps", "list_all_rs", "list_all_ts", "list_all_us"]
# functions to query a record by id
__all__ += ["list_hl_by_id", "list_ms_by_id", "list_mr_by_id", "list_ps_by_id", "list_rs_by_id", "list_ts_by_id", "list_us_by_id"]
# functions to create a record
__all__ += ["create_us"]
# function to update a record
__all__ += ["update_us", "update_ps", "update_rs"]
# function to delete a record
__all__ += ["delete_us", "delete_ps", "delete_rs"]