<script lang="ts">
	import { onMount } from 'svelte';
	import anime from 'animejs';

	onMount(async () => {
		anime({
			targets: '.animejs__account__icon',
			color: '#FFFFFF',
			scale: 1.5
		});
		anime({
			targets: '.animejs__password__icon',
			color: '#FFFFFF',
			scale: 1.5
		});
	});
	// Declare variables here
	let passwordType: 'password' | 'text' = 'password';

	// bound variables
	let email: string = '';
	let password: string = '';

	const handleEyeClick = () => {
		switch (passwordType) {
			case 'password':
				passwordType = 'text';
				break;
			case 'text':
				passwordType = 'password';
				break;
		}
	};

	const handleEmail = (e) => {
		email = e?.target?.value;
	};
	const handlePassword = (e) => {
		password = e?.target?.value;
	};

	const handleFormSubmit = (e) => {
		console.log(email, password);
	};
</script>

<form method="POST" on:submit|preventDefault={handleFormSubmit}>
	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left">
					<input class="input" placeholder="Username" type="text" on:input={handleEmail} />

					<span class="icon is-small is-left">
						<ion-icon class="animejs__account__icon" name="person-circle-outline" />
					</span>
				</p>
			</div>
		</div>
	</div>
	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left has-icons-right">
					<input
						class="input"
						placeholder="Password"
						type={passwordType?.toLowerCase()}
						on:input={handlePassword}
					/>
					<span
						class="
                            icon
                            is-small is-right is-clickable is-unselectable
                        "
						on:click={handleEyeClick}
					>
						👀
					</span>
					<span class="icon is-small is-left">
						<ion-icon class="animejs__password__icon" name="lock-closed-outline" />
					</span>
				</p>
			</div>
		</div>
	</div>
	<div class="items columns is-mobile is-centered">
		<div class="column is-narrow">
			<button id="button" class="button is-rounded is-centered is-ghost"> Sign in </button>
		</div>
	</div>
</form>
<div class="level">
	<div class="level-left">
		<div class="level-item is-size-7">
			<span class="has-text-link">
				<!-- <a class="href_tag" href="#"> Forgot password? </a> -->
			</span>
		</div>
	</div>
	<div class="level-right">
		<div class="level-item is-size-7">
			<p class="new_here_tag">
				New here?
				<span class="has-text-link">
					<a class="href_tag" href="register"> Register an account </a>
				</span>
			</p>
		</div>
	</div>
</div>
