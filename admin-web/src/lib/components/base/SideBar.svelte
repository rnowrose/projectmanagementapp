<script lang="ts">
  import {
      faCodeBranch,
      faColumns,
      faListCheck,
      faPlus,
      faRocket,
      faTasks
  } from '@fortawesome/free-solid-svg-icons';
  import { Fa } from 'svelte-fa';
</script>

<aside class="bg-base-200 fixed left-0 top-16 bottom-0 flex flex-col">
  <ul class="menu p-4 flex-1 space-y-2">
    <li class="w-full">
      <a class="hover:bg-secondary hover:text-white transition-colors" href="#">
        <Fa icon={faListCheck}/>
        Backlog
      </a>
    </li>
    <li class="w-full">
      <a class="hover:bg-secondary hover:text-white transition-colors" href="#">
        <Fa icon={faColumns}/>
        Board
      </a>
    </li>
    <li class="w-full">
      <a class="hover:bg-secondary hover:text-white transition-colors" href="#">
        <Fa icon={faRocket}/>
        Release
      </a>
    </li>
    <li class="w-full">
      <a class="hover:bg-secondary hover:text-white transition-colors" href="#">
        <Fa icon={faCodeBranch} />
        Repository
      </a>
    </li>
    <li class="w-full">
      <a class="hover:bg-secondary hover:text-white transition-colors" href="#">
        <Fa icon={faTasks} />
        Tasks
      </a>
    </li>
  </ul>
  
  <!-- Add Item Button at bottom -->
  <div class="p-4 border-t border-base-300">
    <button class="btn btn-primary w-full">
      <Fa icon={faPlus} class="h-5 w-5" />
      Add Item
    </button>
  </div>
</aside>