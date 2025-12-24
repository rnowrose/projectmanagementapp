<script lang="ts">
    import Modal from "$lib/components/base/Modal.svelte";
    

    interface Props {
        githibUrl: string;
        linkedinUrl: string;
        websiteUrl: string;
        updateUser: () => Promise<void>;
    }
    
    let { githibUrl = '', linkedinUrl = '', websiteUrl = '' } = $props();

</script>
<Modal title="Edit Additional Information">
    <form class="fieldset bg-base-200 border-base-300 w-100 border p-4">
        <div class="form-control w-full mb-4">
            <label class="label" for="githubUrl">GitHub URL</label>
            <input
                id="githubUrl"
                type="url"
                class="input w-full"
                placeholder="GitHub URL"
                bind:value={githibUrl}
            />
        </div>
        <div class="form-control w-full mb-4">
            <label class="label" for="linkedinUrl">LinkedIn URL</label>
            <input
                id="linkedinUrl"
                type="url"
                class="input w-full"
                placeholder="LinkedIn URL"
                bind:value={linkedinUrl}
            />
        </div>
        <div class="form-control w-full mb-4">
            <label class="label" for="websiteUrl">Website URL</label>
            <input
                id="websiteUrl"
                type="url"
                class="input w-full"
                placeholder="Website URL"
                bind:value={websiteUrl}
            />
        </div>
        <div class="modal-action">
            <button class="btn btn-primary" type="submit">Save</button>
        </div>
    </form>
</Modal>
