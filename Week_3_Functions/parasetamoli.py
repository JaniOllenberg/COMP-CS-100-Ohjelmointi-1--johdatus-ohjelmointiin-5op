"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
Jani Ollenberg
H288244
"""

def calculate_dose(weight, time, total_doze_24):
	"""
	Calculates the dose to give
	"""
	full_dose = 15 * weight
	if total_doze_24 + full_dose > 4000:
		return full_dose - (total_doze_24 + full_dose - 4000)
	else:
		if time >= 6:
			return full_dose
		else:
			return 0
			
def main():
	weight = int(input("Patient's weight (kg): "))
	time = int(input("How much time has passed from the previous dose (full hours): "))
	total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))

	doze_to_give = calculate_dose(weight, time, total_doze_24)
	print(f"The amount of Parasetamol to give to the patient: {doze_to_give}")

	# calculate_dose assumes parameters to be of type int
	# and they should be passed in the order: weight, time, total_doze_24
	# (or more like the automated tests assume this)


if __name__ == "__main__":
	main()
