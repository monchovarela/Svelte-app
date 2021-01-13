<script>
    import Data from "../data.json";
</script>

<style>
    section {
        padding: 1rem;
    }
    h3,
    p {
        margin: 0;
    }
    a,span{
        text-decoration: none;
        color:orangered;
        transition:all 500ms ease;
    }
    a:hover{
        border-bottom:1px solid orangered;
        transition:all 500ms ease;
    }
    .back{
        display:block;
        max-width:10rem;
        margin:2rem auto;
        padding:0.4rem 0.8rem;
        text-align:center;
        border:1px solid orangered;
        color: orangered;
        transition:all 500ms ease;
    }
    .back:hover{
        background: orangered;
        color: white;
        transition:all 500ms ease;
    }
</style>

<section>
    <h3>{Data.about_title}</h3>
    <p>{Data.about_desc}</p>
    <p>
        <b>Instagram: </b> <span>{Data.author}</span><br/>
        <a href="/" class="back">Back to home</a>
    </p>
</section>
