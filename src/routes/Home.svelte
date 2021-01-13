<script>
    import Data from "../data.json";
</script>

<style>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: calc(100% - 3rem);
        height: 20rem;
    }
    img,
    p {
        margin: 0;
    }
    img {
        width: 10rem;
    }
    a {
        text-decoration: none;
        color: orangered;
        transition: all 500ms ease;
    }
    a:hover {
        border-bottom: 1px solid orangered;
        transition: all 500ms ease;
    }
</style>

<section>
    <img src="svelte-logo-horizontal.svg" alt="" />
    <p>{Data.desc}</p>
    <p>{Data.made} <a href="/about">{Data.author}</a></p>
</section>
