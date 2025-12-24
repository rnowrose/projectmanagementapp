<script lang="ts">
  import { userStore } from '$lib/stores/userStore';
  import { goto } from '$app/navigation';

  function logout() {
    userStore.logout().then(() => {
      goto('/users/login');
    });
  }
</script>
<div class="dropdown dropdown-end">
      <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
        <div class="w-10 rounded-full">
          <img
            alt="Tailwind CSS Navbar component"
            src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
        </div>
      </div>
      <ul
        tabindex="-1"
        class="menu menu-sm dropdown-content bg-primar rounded-box z-1 mt-3 w-52 p-2 shadow">
        <li>
          <a href="/users/profile">
            Profile
          </a>
        </li>
        <li><a href="/users/login" onclick={logout}>Logout</a></li>
      </ul>
</div>