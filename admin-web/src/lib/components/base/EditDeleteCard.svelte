<script lang="ts">
      import { faPenToSquare, faTrashCan } from '@fortawesome/free-solid-svg-icons';
      import { Fa } from 'svelte-fa';
    import Confirmation from './Confirmation.svelte';

    interface CardProps {
        title: string;
        editModal?: () => void;
        deleteData: () => void;



        // You can define any props you want to pass to the Card component here
    }
    let { title, buttonName, needsButton, editModal, delete: deleteFn }: CardProps = $props();
    
  // No additional script logic needed for this simple card component
</script>
<div class="card bg-base-100 w-96 shadow-sm">
    <div class="card-body">
        <h2 class="card-title">{title}</h2>
        <slot></slot>
        <div class="card-actions">
            <button class="btn btn-primary" onclick={editModal}><Fa icon={faPenToSquare} class="h-4 w-4" /></button>
        </div>
        <div class="card-actions justify-end">
            <button class="btn btn-primary" onclick={() => confirmationModal.showModal()}><Fa icon={faTrashCan} class="h-4 w-4" /></button>
            <dialog bind:this={confirmationModal} class="modal">
                <Confirmation deleteData={deleteData} />
            </dialog>
        </div>

    </div>
</div>