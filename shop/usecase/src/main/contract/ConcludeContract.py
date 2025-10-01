from abc import ABC


class ConcludeContract(ABC):
    real_estate_owner: str
    agency: str
    real_estate: str
    def invoke(self) -> AgencyContract :pass

    """
    собственник и агенство "заключают договор" (conclude contract) 
        об оказании услуг по продаже/аренде недвижимости,
    полсе этого:
        Уведомить владельца объявления, которое необходимо снять с публикации 
            (Notify_owner_that_needs_removed_advert_from_publication);
        Уведомить фотографа о том, что нужно сделать фото для объявления
            (Notify_photographer_that_photo_needs_taken_for_advert)
        Уведомить дизайнера о том, что нужно отрисовать планировку
            (Notify_designer_flat_plan_needs_drawn_up)
        Уведомить маркетолога о том, что нужно написать текст объявления
            (Notify_marketer_ad_text_needs_written)    
    """