<script lang="ts">
    import Card from "$lib/components/base/Card.svelte";
    import EditDeleteCard from "$lib/components/base/EditDeleteCard.svelte";
    import EditAdditionalInfo from "./EditAdditionalInfo.svelte";

    interface Props {
        githuburl: string;
        linkedinurl: string;
        websiteurl: string;
        updateUser: () => Promise<void>;
    }
    let { githuburl = '', linkedinurl = '', websiteurl = '', updateUser } = $props();
    let editAdditionalInfoDialog = $state<HTMLDialogElement | null>(null);
</script>


<Card title="Additional User Information" buttonName="Edit Additional Info" needsButton={true}>
    <p><strong>GitHub:</strong> {githuburl}</p>
    <p><strong>LinkedIn:</strong> {linkedinurl}</p>
    <p><strong>Website:</strong> {websiteurl}</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary" onclick={updateUser}>Edit</button>
    </div>
   <dialog bind:this={editAdditionalInfoDialog} id="edit_additional_info" class="modal">
        <EditAdditionalInfo
            githibUrl={githuburl}
            linkedinUrl={linkedinurl}
            websiteUrl={websiteurl}
        />
    </dialog>
</Card>
