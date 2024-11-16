$(document).ready(function() {
    // initial setup

    // initial load or browser refresh for users.html form
    updateRoleFields();

    // event listeners

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
    $("#search").click(function(event) {
        event.preventDefault();
        const userId = $("#searchID").val();
        const table = $("input[name='searchTable']:checked").val();
        getTableDataByID(table, userId);
    });
    $("#create").click(function(event) {
        event.preventDefault();

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

        // player fields
        if ($("#createRole").val() === "player") {
            const playerData = {
                team_id: $("#createTeamID").val(),
                skill_level: $("#createSkillLevel").val(),
                position: $("#createPosition").val()
            };
            userData = {...userData, ...playerData};
        } else if ($("#createRole").val() === "referee") {
            const refereeData = {
                referee_level: $("#createRefereeLevel").val()
            };
            userData = {...userData, ...refereeData};
        }
        console.log(userData);

        createRecord("user", userData);
    });

    $("#delete").click(function(event) {
        event.preventDefault();
        const userId = $("#deleteID").val();
        const table = $("input[name='deleteTable']:checked").val();
        deleteRecord(table, userId);
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

    // helper functions

    // this function makes a GET request to the server to get all the data from a specific table
    function getTableData(table) {
        const ENDPOINT = "/api/" + table + "/read";
        $.ajax({
            url: ENDPOINT,
            type: "GET",
            success: function(resp) {
                renderTable(resp, "allOutput");
            },
            error: function(error) {
                console.error(error);
                $("#buttonOutput").html("No record found");
            }
        });
    }

    function getTableDataByID(table, id) {
        const ENDPOINT = "/api/" + table + "/read/" + id;
        $.ajax({
            url: ENDPOINT,
            type: "GET",
            success: function(resp) {
                renderTable(resp, "searchOutput");
            },
            error: function(error) {
                console.error(error);
                $("#searchOutput").html("No record found");
            }
        });
    }

    function createRecord(table, data) {
        const ENDPOINT = "/api/" + table + "/create";
        $.ajax({
            url: ENDPOINT,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function(resp) {
                console.log(resp);
                $("#createOutput").html("Record created successfully");
            },
            error: function(error) {
                console.error(error);
                $("#createOutput").html("Error creating record");
            }
        });
    }

    function deleteRecord(table, id) {
        const ENDPOINT = "/api/" + table + "/delete/" + id;
        $.ajax({
            url: ENDPOINT,
            type: "DELETE",
            success: function(resp) {
                console.log(resp);
                $("#deleteOutput").html("Record ID " + id + " deleted successfully");
            },
            error: function(error) {
                console.error(error);
                $("#deleteOutput").html("No record ID " + id + " found");
            }
        });
    }

    // this function renders the data in a table format
    function renderTable(data, htmlID) {        
        let table = $("<table class='table table-bordered table-hover'></table>");
        let thead = $("<thead></thead>");
        let tbody = $("<tbody></tbody>");
        let trBody = $("<tr></tr>");
        let trHead = $("<tr></tr>");

        if (data.length > 0) {
            for (let key in data[0]) {
                trHead.append("<th>" + key + "</th>");
            }
    
            thead.append(trHead);
            table.append(thead);

            for (let i = 0; i < data.length; i++) {
                let tr = $("<tr></tr>");
                
                for (let key in data[i]) {
                    tr.append("<td>" + data[i][key] + "</td>");
                }
                
                tbody.append(tr);
            }
            table.append(tbody);
        } else {
            for (let key in data) {
                trHead.append("<th>" + key + "</th>");
            }
            thead.append(trHead);
            table.append(thead);

            for (let key in data) {
                trBody.append("<td>" + data[key] + "</td>");
            }
            tbody.append(trBody);
            table.append(tbody);
        }

        table.append(tbody);
        $("#"+htmlID).html(table);    
    }

    function updateRoleFields() { 
        let role = $("#createRole").val();
        if (role === "player") {
            $("#playerFields").show();
            $("#refereeFields").hide();
        } else if (role === "referee") {
            $("#playerFields").hide();
            $("#refereeFields").show();
        } else {
            $("#playerFields").hide();
            $("#refereeFields").hide();
        }
    }
});