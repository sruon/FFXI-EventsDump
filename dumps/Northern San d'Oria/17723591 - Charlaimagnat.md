# 17723591 - Charlaimagnat

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 304 bytes                     |
| Total Events     | 5                             |
| References Count | 11                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [702](#event-702)     | 0x0001       |      9 |              5 |
| [703](#event-703)     | 0x000A       |     98 |             18 |
| [704](#event-704)     | 0x006C       |     37 |              7 |
| [705](#event-705)     | 0x0091       |     78 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x31F0      |       12784 |
|       1 | 0x0115      |         277 |
|       2 | 0x31F1      |       12785 |
|       3 | 0x0014      |          20 |
|       4 | 0x31F2      |       12786 |
|       5 | 0x31F3      |       12787 |
|       6 | 0x31F4      |       12788 |
|       7 | 0x31F5      |       12789 |
|       8 | 0x31F6      |       12790 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0000      |           0 |

## String References

- **12784**: My name is Charlaimagnat. I am engaged in the translation of ancient texts found in ruins across Vana'diel.
- **12785**: Ah, you must be the adventurer, <Player>. I have recently received correspondence from Alfesar. I believe you have a letter and $6 for me.
- **12786**: As Alfesar reported in his letter, ancient magic is engraved upon this tablet.
- **12787**: However, I will need more time to decipher all the text. I still cannot tell what magic this spell is for.
- **12788**: Please return another day and I shall share with you what I have found. May Altana's providence guide you on your journey.
- **12789**: Ah, <Player>. I have finished deciphering the spell. I give you my thanks for your assistance.
- **12790**: Now that the text is translated, we can produce copies. I would like to offer you one in expression of our gratitude.

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

### Event 702

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A D1 00 1D 00 80 23  21 00                     ......#!.      
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=12784*)
    → "My name is Charlaimagnat. I am engaged in the translation of ancient texts found in ruins across Vana'diel."
  2: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0008 [0x21] END_EVENT
  4: 0x0009 [0x00] END_REQSTACK()
```

### Event 703

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000A   |
| Data Size    | 98 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                42 1A D1 00 03 03            B.....
0010: 10 01 80 1D 02 80 23 5B  03 80 F8 FF FF 7F F8 FF  ......#[........
0020: FF 7F 74 6C 6B 30 1D 04  80 23 1D 05 80 23 5B 03  ..tlk0...#...#[.
0030: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 53 F8 FF  .........tlk1S..
0040: FF 7F F8 FF FF 7F 74 6C  6B 31 1D 06 80 23 5B 03  ......tlk1...#[.
0050: 80 F8 FF FF 7F F8 FF FF  7F 69 6E 6F 30 53 F8 FF  .........ino0S..
0060: FF 7F F8 FF FF 7F 69 6E  6F 30 21 00              ......ino0!.    
```

#### Opcodes

```
  0: 0x000A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000B [0x1A] CALL_SUBROUTINE(address=0x00D1)
  2: 0x000E [0x03] Work_Zone[3] = 277*
  3: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=12785*)
    → "Ah, you must be the adventurer, <Player>. I have recently received correspondence from Alfesar. I believe you have a letter and $6 for me."
  4: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0017 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  6: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=12786*)
    → "As Alfesar reported in his letter, ancient magic is engraved upon this tablet."
  7: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=12787*)
    → "However, I will need more time to decipher all the text. I still cannot tell what magic this spell is for."
  9: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 11: 0x003D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 12: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=12788*)
    → "Please return another day and I shall share with you what I have found. May Altana's providence guide you on your journey."
 13: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x004E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
 15: 0x005D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 16: 0x006A [0x21] END_EVENT
 17: 0x006B [0x00] END_REQSTACK()
```

### Event 704

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 37 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      1A D1 00 1D              ....
0070: 06 80 23 5B 03 80 F8 FF  FF 7F F8 FF FF 7F 69 6E  ..#[..........in
0080: 6F 30 53 F8 FF FF 7F F8  FF FF 7F 69 6E 6F 30 21  o0S........ino0!
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x006C [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x006F [0x1D] PRINT_EVENT_MESSAGE(message_id=12788*)
    → "Please return another day and I shall share with you what I have found. May Altana's providence guide you on your journey."
  2: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0073 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0082 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
  5: 0x008F [0x21] END_EVENT
  6: 0x0090 [0x00] END_REQSTACK()
```

### Event 705

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 78 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    42 1A D1 00 03 03 10  01 80 1D 07 80 23 5B 03   B...........#[.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 69 6E 6F 30 1D 08 80  .........ino0...
00B0: 23 45 09 80 F0 FF FF 7F  F0 FF FF 7F 71 73 74 63  #E..........qstc
00C0: 0A 80 53 F8 FF FF 7F F8  FF FF 7F 69 6E 6F 30 21  ..S........ino0!
00D0: 00 86 00 F8 FF FF 7F 1E  F0 FF FF 7F 6F 70 1B     ............op. 
```

#### Opcodes

```
  0: 0x0091 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0092 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  2: 0x0095 [0x03] Work_Zone[3] = 277*
  3: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=12789*)
    → "Ah, <Player>. I have finished deciphering the spell. I give you my thanks for your assistance."
  4: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
  6: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=12790*)
    → "Now that the text is translated, we can produce copies. I would like to offer you one in expression of our gratitude."
  7: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x00C2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 10: 0x00CF [0x21] END_EVENT
 11: 0x00D0 [0x00] END_REQSTACK()

SUBROUTINE_00D1:
 12: 0x00D1 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
 13: 0x00D7 [0x1E] EventEntity looks at LocalPlayer and starts talking
 14: 0x00DC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x00DD [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 16: 0x00DE [0x1B] RETURN
```
