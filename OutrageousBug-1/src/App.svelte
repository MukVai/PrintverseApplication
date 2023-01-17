<script>
  import logo from "./assets/nanofactory-logo.svg";
  import Counter from "./lib/Counter.svelte";
  import Header from "./lib/Header.svelte";
  import { words } from "./words.js";

  let r = 13;
  let g = 83;
  let b = 154;
  $: color = `rgb(${r}, ${g}, ${b})`;

  setInterval(() => {
    r = Math.random() * 255;
    g = Math.random() * 255;
    b = Math.random() * 255;
  }, 750);

  $: title = words[Math.floor(r) + Math.floor(g) + Math.floor(b)];
</script>

<Header {title} />
<main id="main">
  <img src={logo} alt="Svelte Logo" />
  <h1 style:color id="hello">Hello Dev!</h1>

  <Counter {title} />

  <p>
    Check out <a href="https://nanofactory.printerverse.net">NanoFactory</a> here.
  </p>
</main>

<style>
  * {
    box-styling: border-box;
    padding: 0;
    margin: 0;
  }
  :root {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  }

  main {
    text-align: center;
    background-color: #202020;
    color: white;
    height: 99vh;
    width: 99vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  :global(body) {
    margin: 0;
  }

  img {
    width: 16rem;
  }

  h1 {
    text-transform: uppercase;
    font-size: 4rem;
    font-weight: 100;
    line-height: 1.1;
    margin: 2rem auto;
    max-width: 14rem;
  }

  p {
    max-width: 14rem;
    margin: 1rem auto;
    line-height: 1.35;
  }

  @media (min-width: 480px) {
    h1 {
      max-width: none;
    }

    p {
      max-width: none;
    }
  }
</style>
