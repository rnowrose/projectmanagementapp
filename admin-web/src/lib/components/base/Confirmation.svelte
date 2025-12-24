<script lang="ts">
    interface Props {
        deleteData : () => void;
    }
    let { deleteData } = $props();
</script>

<div class="card bg-neutral text-neutral-content w-96">
  <div class="card-body items-center text-center">
    <h2 class="card-title">Confirm Action</h2>
    <p>Are you sure you want to proceed?</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary" onclick={deleteData}>Confirm</button>
      <form method="dialog">
        <button class="btn btn-ghost">Cancel</button>
      </form>
    </div>
  </div>
</div>