import { updateDatabase, updateRoleFields, getTableData, getTableDataByID, deleteRecord, createRecord } from "./utils.js";

$(document).ready(function() {
    // initial setup

    // initial load or browser refresh for users.html form
    updateRoleFields();

    // event listeners

    // index.html
    $("#dropdb").click(function() {
        updateDatabase("drop");
    });
    $("#createdb").click(function() {
        updateDatabase("create");
    });
    $("#populatedb").click(function() {
        updateDatabase("populate");
    });
    $("#queriesdb").click(function() {
        updateDatabase("queries");
    });

    // search, delete, create button functionality 
    // (users.html, teams.html, house_league.html, match_stats.html, match_referee.html)
    $("#search").click(function(event) {
        event.preventDefault();
        const userId = $("#searchID").val();
        const buttonValue = $("#search").val();
        const radioSelect = $("input[name='searchTable']:checked").val();
        
        getTableDataByID(radioSelect ? radioSelect : buttonValue, userId);
    });
    $("#delete").click(function(event) {
        event.preventDefault();
        const userId = $("#deleteID").val();
        const deleteButton = $("input[name='deleteTable']:checked").val();
        deleteRecord(deleteButton, userId);
    });
    $("#create").click(function(event) {
        event.preventDefault();

        if ($("#createUserID").val()){
            let userData = {
                user_id: $("#createID").val(),
                first_name: $("#createFirstName").val(),
                last_name: $("#createLastName").val(),
                age: $("#createAge").val(),
                email_address: $("#createEmail").val(),
                password: $("#createPassword").val(),
                date_of_birth: $("#createDOB").val(),
                role: $("#createRole").val(),
            };

            if ($("#createRole").val() === "player") {
                const playerData = {
                    team_id: $("#createTeamID").val(),
                    skill_level: $("#createSkillLevel").val(),
                    position: $("#createPosition").val()
                };
                userData = {...userData, ...playerData};
            } else if ($("#createRole").val() === "referee") {
                const refereeData = {
                    experience_level: $("#createExperienceLevel").val()
                };
                userData = {...userData, ...refereeData};
            }

            createRecord("user", userData);
        } else if ($("#createTeamID").val()){ //Creates a team entry if teamId exists
            let teamData = {
                team_id: $("#createTeamID").val(),
                team_name: $("#createTeamName").val(),
                skill_level:  $("#createTeamSkill").val(),
            }; 
            
            createRecord("team", teamData);
        } else if ($("#createMatchID").val()){ //cre
            let hlData = {
                match_id: $("#createMatchID").val(),
                match_date: $("#createMatchDate").val(),
                skill_level: $("#createTeamSkill").val(),
                ht_id: $("#createHTID").val(),
                at_id: $("#createATID").val(),
                ht_score: $("#createHTScore").val(),
                at_score: $("#createATScore").val(),
            }
            
            createRecord("house-league", hlData);
        
        } else if ($("#createRefID").val()){ //make sure that the REF ID exists
            let mrData = {
                match_id: $("#createMID").val(),
                referee_id: $("#createRefID").val(),
            }
            console.log(mrData);
            createRecord("match-referees", mrData);
        }
        
    });

    // users.html
    $("#allUS").click(function() {
        getTableData("user");
    });
    $("#allPS").click(function() {
        getTableData("player");
    });
    $("#allRS").click(function() {
        getTableData("referee");
    });
    $("#createRole").change(function() {
        updateRoleFields();
    });

    // teams.html
    $("#allTS").click(function() {
        getTableData("team");
    });

    // house_league.html
    $("#allHL").click(function() {
        getTableData("house-league");
    });

    // match_stats.html
    $("#allMS").click(function() {
        getTableData("match-stats");
    });

    // match_referee.html
    $("#allMR").click(function() {
        getTableData("match-referees");
    });
});