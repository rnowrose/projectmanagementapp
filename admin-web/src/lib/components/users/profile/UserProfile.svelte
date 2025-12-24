<script lang="ts">
    import UpdateUserInfo from "$lib/components/users/profile/UpdateUserInfo.svelte";

    interface Props {
        fullName: string;
        email: string;
        phoneNumber?: string;
        username: string;
        updateUser: () => Promise<void>; 
    }

    let { fullName, email, phoneNumber = '', username, updateUser } = $props();

    let updateUserDialog: HTMLDialogElement;

</script>
<div class="card bg-base-100 w-96 shadow-sm">
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
      alt="Shoes" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">{fullName}</h2>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Email:</strong> {email}</p>
    {#if phoneNumber}
    <p><strong>Phone:</strong> {phoneNumber}</p>
    {/if}
    <div class="card-actions justify-end">
      <button class="btn btn-primary" onclick={() => updateUserDialog.showModal()}>Update Profile</button>
      <dialog bind:this={updateUserDialog} id="update_user" class="modal">
        <UpdateUserInfo 
            {fullName}
            {email}
            {phoneNumber}
            {username}
            {updateUser}
        />
      </dialog>
    </div>
  </div>
</div>