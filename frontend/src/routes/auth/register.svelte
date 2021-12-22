<script lang="ts">
	import characterA from '$lib/assets/svg/character_a.svg';
	import characterZ from '$lib/assets/svg/character_z.svg';

	import { onMount } from 'svelte';
	import anime from 'animejs';

	onMount(async () => {
		anime({
			targets: '.animejs__character__a__icon',
			scale: 0.8
		});
		anime({
			targets: '.animejs__character__z__icon',
			scale: 0.8,
			translateY: -1
		});
		anime({
			targets: '.animejs__username__icon',
			color: '#FFFFFF',
			scale: 1.6
		});
		anime({
			targets: '.animejs__mail__icon',
			color: '#FFFFFF',
			scale: 1.4
		});
		anime({
			targets: '.animejs__password__one__icon',
			color: '#FFFFFF',
			scale: 1.4
		});
		anime({
			targets: '.animejs__password__two__icon',
			color: '#FFFFFF',
			scale: 1.7
		});
	});
</script>

<form method="POST" x-trap="true">
	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left">
					<!-- {{ form.first_name }} -->
					<input type="text" class="input" />

					<span class="icon is-small is-left">
						<img alt="A" class="animejs__character__a__icon" src={characterA} />
					</span>
				</p>
			</div>
		</div>
	</div>
	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left">
					<!-- {{ form.last_name }} -->
					<input type="text" class="input" />

					<span class="icon is-small is-left">
						<img alt="Z" class="animejs__character__z__icon" src={characterZ} />
					</span>
				</p>
			</div>
		</div>
	</div>
	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left">
					<!-- {{ form.username }} -->
					<input type="text" class="input" />
					<span class="icon is-small is-left">
						<ion-icon class="animejs__username__icon" name="person-circle-outline" />
					</span>
				</p>
			</div>
		</div>
	</div>

	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left">
					<input type="email" class="input" />

					<span class="icon is-small is-left">
						<ion-icon class="animejs__mail__icon" name="mail-outline" />
					</span>
				</p>
			</div>
		</div>
	</div>

	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left">
					<input type="password" class="input" />

					<span class="icon is-small is-left">
						<ion-icon class="animejs__password__one__icon" name="lock-closed-outline" />
					</span>
				</p>
			</div>
		</div>
	</div>
	<div class="items field is-horizontal">
		<div class="field-body">
			<div class="field">
				<p class="control is-expanded has-icons-left">
					<input type="password" class="input" />
					<span class="icon is-small is-left">
						<ion-icon class="animejs__password__two__icon" name="document-lock-outline" />
					</span>
				</p>
			</div>
		</div>
	</div>

	<div class="items columns is-mobile is-centered">
		<div class="column is-narrow">
			<button id="button" class="button is-rounded is-centered is-ghost"> Register </button>
		</div>
	</div>
</form>
