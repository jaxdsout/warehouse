from rest_framework import serializers
from .models import Creator, Item, Bid, Event

class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creator
        fields = (
            'id',
            'role',
            'name',
            'website',
            'about',
            'items'
        )

class BidSerializer(serializers.HyperlinkedModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        source='item'
    )
    
    current_bid = serializers.SerializerMethodField()
    
    class Meta:
        model = Bid
        fields = (
            'id',
            'item_id',
            'amount',
            'current_bid',
            'time'
        )

    def get_current_bid(self, obj):
        return obj.item.current_price if obj.item else None
    

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    bids = BidSerializer(many=True, read_only=True)
    
    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Creator.objects.all(),
        source='creator'
    )

    class Meta:
        model = Item
        fields = (
            'id',
            'category',
            'title',
            'creator_name',
            'creator_id',
            'description',
            'creation_period',
            'materials_used',
            'dimensions',
            'listing_start',
            'listing_end',
            'current_price',
            'starting_price',
            'image',
            'bids'
        )

    def get_creator_name(self, obj):
        return obj.creator.name if obj.creator else None

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'poster',
            'time',
            'creator'
        )