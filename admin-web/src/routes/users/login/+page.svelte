<script lang="ts">
  import { goto } from '$app/navigation';
  import type { LoginInfo } from '$lib/domain/Users.ts';
  import { loginSchema } from '$lib/schema/auth.schema.ts';
  import { userStore } from '$lib/stores/userStore.ts';

  let username = $state<string>('');
  let password = $state<string>('');
  let message = $state<string>('');
  let success = $state<boolean>(false);

  function authenticate() {
    const result = loginSchema.safeParse({ username, password });
    if (!result.success) {
      message = 'Invalid username or password';
      return;
    }

    userStore.login({ username, password }).then((loginInfo: LoginInfo | null) => {
      if (loginInfo) {
        message = loginInfo.message ;
        success = true;
        goto('/');
      } else {
        message = 'Invalid credentials' ;
      }
    }).catch((error) => {
      message = 'Authentication failed';
      console.error('Authentication failed:', error);
    });
  }
</script>
{#snippet alert(message: string, success: boolean)}
  <div role="alert" class="alert {success ? 'alert-success' : 'alert-error'}">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
    <span>{message}</span>
  </div>
{/snippet}

<div class="min-h-screen flex items-center justify-center">
  <form class="fieldset bg-base-200 border-base-300 rounded-box w-100 border p-4">
      <div class="card w-full">
        <figure class="px-10 pb-2">
          <img src="../admin-cat.png" alt="Login" />
        </figure>
        <div class="divider">Login</div>
        <div class="card-body"> 
        {#if message}
         {@render alert(message, success)}
        {/if}
          <label class="label" for="username">Username</label>
          <input id="username" type="text" class="input" placeholder="Username" bind:value={username} />

          <label class="label" for="password">Password</label>
          <input id="password" type="password" class="input" placeholder="Password" bind:value={password} />
        </div>
        <div class="card-actions justify-center">
          <button class="btn btn-primary" type="button" onclick={authenticate}>Login</button>
        </div>
      </div>
      <div class="mt-4 text-center">
          Don't have an account?
          <a href="/users/register" class="btn btn-primary btn-xs">Sign up</a>
      </div>   
  </form>
</div>
