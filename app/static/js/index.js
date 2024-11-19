$(document).ready(function() {
    // initial setup

    // initial load or browser refresh for users.html form
    updateRoleFields();

    // event listeners

    // index.html
    $("#dropdb").click(function() {
        changeDatabase("drop");
    });
    
    $("#createdb").click(function() {
        changeDatabase("create");
    });
    
    $("#populatedb").click(function() {
        changeDatabase("populate");
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
    $("#search").click(function(event) {
        event.preventDefault();
        const userId = $("#searchID").val();
        const table = $("input[name='searchTable']:checked").val();
        getTableDataByID(table, userId);
    });
    $("#create").click(function(event) {
        event.preventDefault();

        if ($("#createID").val()){//Checks to see if UserId exists, this means that we want to create a user entry
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
                    experience_level: $("#createExperienceLevel").val()
                };
                userData = {...userData, ...refereeData};
            }

            console.log(userData);

            createRecord("user", userData);


        } else if ($("#createTeamID").val()){ //Creates a team entry if teamId exists
            let teamData = {
                team_id: $("#createTeamID").val(),
                team_name: $("#createTeamName").val(),
                skill_level:  $("#createTeamSkill").val(),
            }; 
            
            console.log(teamData);
            createRecord("team", teamData);
        }
        
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
                renderTable(table, resp, "allOutput");
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
                renderTable(table, resp, "searchOutput");
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

    function updateRecord(table, id, data) {
        const ENDPOINT = "/api/" + table + "/update/" + id;
        $.ajax({
            url: ENDPOINT,
            type: "PUT",
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function(resp) {
                console.log(resp);
                $("#changeRowOutput").html("Cell updated successfully");
            },
            error: function(error) {
                console.error(error);
                $("#changeRowOutput").html("Error updating cell. Please try again.");
            }
        });
    }

    function deleteRecord(table, id, row) {
        const ENDPOINT = "/api/" + table + "/delete/" + id;

        console.log(ENDPOINT);
        
        $.ajax({
            url: ENDPOINT,
            type: "DELETE",
            success: function(resp) {
                console.log(resp);
                row.remove();
            },
            error: function(error) {
                console.error(error);
                $("#changeRowOutput").html("Error deleting record");
            }
        });
    }

    function changeDatabase(action) {
        const ENDPOINT = "/api/menu/" + action;
        $.ajax({
            url: ENDPOINT,
            type: "POST",
            success: function(resp) {
                console.log(resp);
                $("#resultDB").html(resp.message);
            },
            error: function(error) {
                console.error(error);
                $("#resultDB").html("Error in changing database");
            }
        });
    }

    // this function renders the data in a table format
    function renderTable(specificTable, data, htmlID) {        
        let table = $("<table class='table table-bordered table-hover'></table>");
        let thead = $("<thead></thead>");
        let tbody = $("<tbody></tbody>");
        let trBody = $("<tr></tr>");
        let trHead = $("<tr></tr>");

        if (data.length > 0) {
            for (let key in data[0]) {
                trHead.append("<th>" + key + "</th>");
            }
            trHead.append("<th>Delete</th>");
    
            thead.append(trHead);
            table.append(thead);

            for (let i = 0; i < data.length; i++) {
                let tr = $("<tr></tr>");
                
                for (let key in data[i]) {
                    let td = $("<td contenteditable='true'></td>").text(data[i][key]);
                    td.on("focus", function() {
                        $(this).data("originalValue", $(this).text());
                    });
                    td.on("blur", function() {
                        let newValue = $(this).text();
                        let originalValue = $(this).data("originalValue");
                        if (newValue !== originalValue) {
                            let userId = $(this).closest("tr").find("td:first").text();
                            let updateData = {};
                            updateData[key] = newValue;
                            updateRecord(specificTable, userId, updateData);
                        }
                    });
                    tr.append(td);

                    if (key === Object.keys(data[i])[Object.keys(data[i]).length - 1]) {
                        let deleteBtn = $("<button class='btn btn-danger'>Delete</button>");
                        deleteBtn.on("click", function() {
                            let userId = $(this).closest("tr").find("td:first").text();
                            deleteRecord(specificTable, userId, $(this).closest("tr"));
                        });
                        
                        let tdDelete = $("<td></td>").append(deleteBtn);
                        tr.append(tdDelete);
                    }
                }

                tbody.append(tr);
            }
        } else {
            for (let key in data) {
                trHead.append("<th>" + key + "</th>");
            }
            
            thead.append(trHead);
            table.append(thead);

            for (let key in data) {
                let td = $("<td contenteditable='true'></td>").text(data[key]);
                td.on("focus", function() {
                    $(this).data("originalValue", $(this).text());
                });
                td.on("blur", function() {
                    let newValue = $(this).text();
                    let originalValue = $(this).data("originalValue");
                    if (newValue !== originalValue) {
                        let userId = $(this).closest("tr").find("td:first").text();
                        let updateData = {};
                        updateData[key] = newValue;
                        updateRecord(specificTable, userId, updateData);
                    }
                });
                trBody.append(td);
            }
            tbody.append(trBody);
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