<script>
  export let text = {}
</script>


{#each Object.keys(text) as key}
  <div>
    {#if text[key]}
      {key}
    {/if}
  </div>
{/each}


<style>
  * {
    display: flex;
    flex-direction: column;
  }
</style>