

class CouncludeContractUseCaseTest():
    def test_successfully_conclude (self):
        contract_id: ContractId = ContractId(1)
        agent = Agent('agentFio')
        real_estate_owner = RealEstateOwner('OwnerFio')
        contract: AgencyContract = AgencyContract.Conclude(
            agent
            real_estate_owner,
            contract_id
        )
        reading_store =  ReadingContractStore(contract)
        saving_store = SavingContractStore(contract)
        id_provider = ContractIdProvider()

        usecase = ConcludeContractUseCase(reading_store, saving_store)
        result = usecase.invoke(
            agent: str,
            real_estate_owner: str,
            id_provider
        )
        events = contract.pop_events()
        savedContract = saving_store._contracts[contract.id]

        assert result.is_right() is True
        assert events is not None
        assert savedContract._agent  == contract._agent
        assert savedContract._real_estate_owner  == contract._real_estate_owner
        assert savedContract._id  == contract._id
        assert savedContract.state == ContractStates.Concluded

        assert isinstance(events.by_index(0), ConcludedContractDomainEvent(contract.id))


        assert isinstance (events.by_index(1),
                           Notify_owner_that_needs_removed_advert_from_publication(contract.id))

        assert isinstance(events.by_index(2),
                      Notify_photographer_that_photo_needs_taken_for_advert(contract.id))

        assert isinstance(events.by_index(3),
                          Notify_designer_flat_plan_needs_drawn_up(contract.id))

        assert isinstance(events.by_index(4),
                      Notify_marketer_ad_text_needs_written(contract.id))

    def test_contract_not_found (self):
        contract_id: ContractId = ContractId(1)
        agent = Agent('agentFio')
        real_estate_owner = RealEstateOwner('OwnerFio')
        contract: AgencyContract = AgencyContract.Conclude(
            agent
            real_estate_owner,
            contract_id
        )
        reading_store = ReadingContractStore(contract)
        saving_store = SavingContractStore(contract)
        id_provider = ContractIdProvider()
        usecase = ConcludeContractUseCase(reading_store, saving_store)
        result = usecase.invoke(
            agent: str,
            real_estate_owner: str,
            id_provider
        )

        assert result.is_left()
        assert isinstance(result.value, ConcludeContractUseCaseError.RealEstateOwnerNotFound())
        assert saving_store.contracts is None