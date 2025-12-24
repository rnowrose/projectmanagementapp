<script lang="ts">
  import { faSearch, faSignIn } from '@fortawesome/free-solid-svg-icons';
  import { Fa } from 'svelte-fa';
  import AuthMenu from './AuthMenu.svelte';
</script>
<div class="navbar bg-primary shadow-sm sticky top-0 z-50">
  <div class="flex-1">
      <div class="flex items-center gap-2">
        <img src="/admin-cat.png" alt="Admin Cat Logo" class="w-12 h-11" />
        <a href="/" class="btn btn-ghost text-xl text-secondary hover:text-secondary">Rownok Admin</a>
        <select class="select select-secondary">
          <option disabled selected>Select Project</option>
          <option>Zig</option>
          <option>Go</option>
          <option>Rust</option>
        </select>  
      </div>
  </div>
  <div class="flex-none">
    <div class="flex gap-2">
              <div class="relative">
            <input 
              type="text" 
              placeholder="Search" 
              class="input input-bordered w-64 pl-10" 
            />
            <div class="absolute left-3 top-1/2 -translate-y-1/2">
              <Fa icon={faSearch} class="text-gray-500" />
            </div>
          </div>
          <div>
          
          <AuthMenu />
          </div>
    </div>
  </div>
</div>