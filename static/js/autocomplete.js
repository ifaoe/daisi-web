function ProjectComplete() {
    $('[auto="projects"]').autocomplete({
        source: "/api/get_sessions/",
        minLength: 2,
    });
};
