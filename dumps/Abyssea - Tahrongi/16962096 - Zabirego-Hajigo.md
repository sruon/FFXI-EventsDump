# 16962096 - Zabirego-Hajigo

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 252 bytes                   |
| Total Events     | 3                           |
| References Count | 20                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [407](#event-407)     | 0x0001       |    127 |             43 |
| [500](#event-500)     | 0x0080       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1FB4      |        8116 |
|       2 | 0x1FB5      |        8117 |
|       3 | 0x1FB6      |        8118 |
|       4 | 0x0001      |           1 |
|       5 | 0x1FB7      |        8119 |
|       6 | 0x1FB8      |        8120 |
|       7 | 0x0002      |           2 |
|       8 | 0x1FB9      |        8121 |
|       9 | 0x1FBA      |        8122 |
|      10 | 0x0003      |           3 |
|      11 | 0x1FBB      |        8123 |
|      12 | 0x1FBC      |        8124 |
|      13 | 0x0004      |           4 |
|      14 | 0x1FBD      |        8125 |
|      15 | 0x1FBE      |        8126 |
|      16 | 0x0005      |           5 |
|      17 | 0x1FBF      |        8127 |
|      18 | 0x1FC0      |        8128 |
|      19 | 0x1FD7      |        8151 |

## String References

- **8116**: <Player>? Never heard of [her/him]. Oh, that's you?
- **8117**: You'll have to forgive me. These days, one stranger wandering into our camp looks much like the nextaru.
- **8118**: Our people might seem a bit distant, but that's part and parcel-warcel of living in these harsh times. Help them in their struggle, and they'll learn to trust you in good time.
- **8119**: <Player>-Bo<Player>? Was that the third minister of the Manustery? Oh, I'm sorry. That was you, wasn't it?
- **8120**: You're not a complete stranger-wanger these days, but I fear you haven't made much of an impression. Keep working at it, though, and your day will come.
- **8121**: Wait, don't tell me... <Player>, was it? I've finally-winally managed put a face to the name.
- **8122**: Why, I heard a conversation about you just the other day. "A bit of a bumbler-wumbler, but I suppose [he/she] means well..." they said. It may not sound like much, but you're on the right track. Now is no time to rest in your efforts!
- **8123**: Oh, hullo there, <Player>. I was just talking to a fellow who seemed to have taken quite a liking to you.
- **8124**: Seems it's not often that a stranger has made such an earnestaru attempt to help out. I knew you had it in you, <Player>! Keep working and others will learn to appreciate the work you've done!
- **8125**: Well, if it isn't <Player>! Don't go getting a swelly-welled head, but you've got yourself the makings of your own little fan club these days.
- **8126**: Just goes to show that people appreciataru the good deeds you've done. But I have a feeling we haven't seen the limits of what you can do. Keep showing us what you've got!
- **8127**: <Player>! What a rare treataru! Why, I hear your name everywhere I go these days.
- **8128**: People can't stop talking about how much easier their lives have been since you showed up. No surprise to me, of course. Why, since the first day I spotty-wotted you, I knew this day would come!
- **8151**: Current area score: $0 (Rank $1) Enter a number between 0 and 63. (0 to cancel).

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 407

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 127 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  02 02 10 00 80 80 1F 00   .....op........
0010: 1D 01 80 23 1D 02 80 23  1D 03 80 23 01 7E 00 02  ...#...#...#.~..
0020: 02 10 04 80 80 32 00 1D  05 80 23 1D 06 80 23 01  .....2....#...#.
0030: 7E 00 02 02 10 07 80 80  45 00 1D 08 80 23 1D 09  ~.......E....#..
0040: 80 23 01 7E 00 02 02 10  0A 80 80 58 00 1D 0B 80  .#.~.......X....
0050: 23 1D 0C 80 23 01 7E 00  02 02 10 0D 80 80 6B 00  #...#.~.......k.
0060: 1D 0E 80 23 1D 0F 80 23  01 7E 00 02 02 10 10 80  ...#...#.~......
0070: 80 7E 00 1D 11 80 23 1D  12 80 23 01 7E 00 21 00  .~....#...#.~.!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x001F
  4: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=8116*)
    → "<Player>? Never heard of [her/him]. Oh, that's you?"
  5: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=8117*)
    → "You'll have to forgive me. These days, one stranger wandering into our camp looks much like the nextaru."
  7: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=8118*)
    → "Our people might seem a bit distant, but that's part and parcel-warcel of living in these harsh times. Help them in their struggle, and they'll learn to trust you in good time."
  9: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x001C [0x01] GOTO 0x007E
 11: 0x001F [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0032
 12: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8119*)
    → "<Player>-Bo<Player>? Was that the third minister of the Manustery? Oh, I'm sorry. That was you, wasn't it?"
 13: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=8120*)
    → "You're not a complete stranger-wanger these days, but I fear you haven't made much of an impression. Keep working at it, though, and your day will come."
 15: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x002F [0x01] GOTO 0x007E
 17: 0x0032 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0045
 18: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=8121*)
    → "Wait, don't tell me... <Player>, was it? I've finally-winally managed put a face to the name."
 19: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8122*)
    → "Why, I heard a conversation about you just the other day. "A bit of a bumbler-wumbler, but I suppose [he/she] means well..." they said. It may not sound like much, but you're on the right track. Now is no time to rest in your efforts!"
 21: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0042 [0x01] GOTO 0x007E
 23: 0x0045 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0058
 24: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=8123*)
    → "Oh, hullo there, <Player>. I was just talking to a fellow who seemed to have taken quite a liking to you."
 25: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=8124*)
    → "Seems it's not often that a stranger has made such an earnestaru attempt to help out. I knew you had it in you, <Player>! Keep working and others will learn to appreciate the work you've done!"
 27: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0055 [0x01] GOTO 0x007E
 29: 0x0058 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x006B
 30: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=8125*)
    → "Well, if it isn't <Player>! Don't go getting a swelly-welled head, but you've got yourself the makings of your own little fan club these days."
 31: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=8126*)
    → "Just goes to show that people appreciataru the good deeds you've done. But I have a feeling we haven't seen the limits of what you can do. Keep showing us what you've got!"
 33: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0068 [0x01] GOTO 0x007E
 35: 0x006B [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x007E
 36: 0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=8127*)
    → "<Player>! What a rare treataru! Why, I hear your name everywhere I go these days."
 37: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=8128*)
    → "People can't stop talking about how much easier their lives have been since you showed up. No surprise to me, of course. Why, since the first day I spotty-wotted you, I knew this day would come!"
 39: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x007B [0x01] GOTO 0x007E

SUBROUTINE_007E:
 41: 0x007E [0x21] END_EVENT
 42: 0x007F [0x00] END_REQSTACK()
```

### Event 500

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 48 13 80 71 12 04 80 07  80 71 13 01 10 21 00     H..q.....q...!. 
```

#### Opcodes

```
  0: 0x0080 [0x48] [System] [8151*]:
    → "Current area score: $0 (Rank $1) Enter a number between 0 and 63. (0 to cancel)."
  1: 0x0083 [0x71] USER_INPUT_HANDLER: Open numerical input with params (work=[1*, 2*])
  2: 0x0089 [0x71] USER_INPUT_HANDLER: Process numerical input B (work=Work_Zone[1])
  3: 0x008D [0x21] END_EVENT
  4: 0x008E [0x00] END_REQSTACK()
```
