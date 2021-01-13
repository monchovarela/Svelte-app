<script>
  // import transition
  import { fade } from "svelte/transition";
  // import router
  import page from "page";
  // pages
  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";
  // json data 
  import Data from "./data.json";

  // set current page
  let current = Home;
  let params;
 
  page("/", () => (current = Home));
  page("/about", () => (current = About));
  page("/*", () => (current = Home));

  // create loader for pywebview
  let status = false;
  setTimeout(
    () =>
      pywebview.api.init("Python is Ready")
      .then((r) => {
        page.start();
        status = true;
      }),
    800
  );

  function closeApp()
  {
    return pywebview.api.close('bye :)');
  }
</script>

<div class="app">
  <div class="app-header pywebview-drag-region">
    <div class="app-title">{Data.title}</div>
    <div class="app-close" on:click={closeApp}>&times;</div>
  </div>
  <div class="app-content">
    {#if status}
      <div transition:fade>
        <svelte:component this={current} {params} />
      </div>
    {:else}
      <div id="loader" transition:fade>
        <div class="preloader" />
      </div>
    {/if}
  </div>
</div>

