const arrows = document.querySelectorAll(".material-symbols-outlined");
const lists = document.querySelectorAll(".list");  

arrows.forEach((material-symbols-outlined, span) => {
    .material-symbols-outlined.addEventListener("click", () => {
        lists[span].style.transform = 'translateX(${
            list[span].computedStyleMap().get("transform")[0].x.value
            -300}px)';
    });
});

z