# 16974379 - Eumoa-Tajimoa

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 176 bytes         |
| Total Events     | 2                 |
| References Count | 10                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [239](#event-239)     | 0x0001       |    108 |             26 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0031      |          49 |
|       2 | 0x1F88      |        8072 |
|       3 | 0x1F89      |        8073 |
|       4 | 0x1F8A      |        8074 |
|       5 | 0x1F8B      |        8075 |
|       6 | 0x0006      |           6 |
|       7 | 0x1F8C      |        8076 |
|       8 | 0x1F8D      |        8077 |
|       9 | 0x1F8E      |        8078 |

## String References

- **8072**: I heard a scary-wary story-wory the other day! You see, a long time ago, the Imperial Army went to fight against the Lamiae on Arrapago Reef...
- **8073**: And they brought a whole bunchy-wunch of automatons to help them fight... I'm still shiver-wivering...
- **8074**: But then comes the reeeally scary part. The battle automatons were charmed by the Lamiae...
- **8075**: Isn't that frighty-wightening? Every last one went crazy for the Lamiae!
- **8076**: I don't want to imagine my Truffle being crazy about anyone but me... I think my hearty-weart would just bursty-wurst!
- **8077**: So I've decided to never, ever go near Arrapago Reef. Anyway, I heard Lamiae can charm Tarutaru, too!
- **8078**: You better look out too, okay? It's a danger-wangerous world we live in.

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

### Event 239

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 108 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 1D 04 80 23 66 01 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
0030: 6C 6B 31 1D 05 80 23 1E  2C 02 03 01 1C 00 80 6E  lk1...#.,......n
0040: 2B 02 03 01 06 80 99 2B  02 03 01 1D 07 80 23 1E  +......+......#.
0050: F0 FF FF 7F 1D 08 80 23  66 01 80 F8 FF FF 7F F8  .......#f.......
0060: FF FF 7F 74 6C 6B 30 1D  09 80 23 21 00           ...tlk0...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=8072*)
    → "I heard a scary-wary story-wory the other day! You see, a long time ago, the Imperial Army went to fight against the Lamiae on Arrapago Reef..."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8073*)
    → "And they brought a whole bunchy-wunch of automatons to help them fight... I'm still shiver-wivering..."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=8074*)
    → "But then comes the reeeally scary part. The battle automatons were charmed by the Lamiae..."
  8: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0024 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
 10: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8075*)
    → "Isn't that frighty-wightening? Every last one went crazy for the Lamiae!"
 11: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0037 [0x1E] EventEntity looks at Truffle (ID: 16974380/0x0103022C) and starts talking
 13: 0x003C [0x1C] WAIT(30* ticks)
 14: 0x003F [0x6E] Eumoa-Tajimoa (ID: 16974379/0x0103022B) uses emote 6*
 15: 0x0046 [0x99] Wait for Eumoa-Tajimoa (ID: 16974379/0x0103022B) animation to complete
 16: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8076*)
    → "I don't want to imagine my Truffle being crazy about anyone but me... I think my hearty-weart would just bursty-wurst!"
 17: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x004F [0x1E] EventEntity looks at LocalPlayer and starts talking
 19: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=8077*)
    → "So I've decided to never, ever go near Arrapago Reef. Anyway, I heard Lamiae can charm Tarutaru, too!"
 20: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0058 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 22: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=8078*)
    → "You better look out too, okay? It's a danger-wangerous world we live in."
 23: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x006B [0x21] END_EVENT
 25: 0x006C [0x00] END_REQSTACK()
```
