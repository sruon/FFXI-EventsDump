# 16883835 - Morangeart

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 148 bytes                   |
| Total Events     | 5                           |
| References Count | 10                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [520](#event-520)     | 0x0001       |     11 |              5 |
| [521](#event-521)     | 0x000C       |     28 |             14 |
| [522](#event-522)     | 0x0028       |     15 |              7 |
| [523](#event-523)     | 0x0037       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2CF7      |       11511 |
|       1 | 0x2CF2      |       11506 |
|       2 | 0x2CF3      |       11507 |
|       3 | 0x2CF4      |       11508 |
|       4 | 0x2CF5      |       11509 |
|       5 | 0x2CF6      |       11510 |
|       6 | 0x2CF0      |       11504 |
|       7 | 0x2CF1      |       11505 |
|       8 | 0x2CEE      |       11502 |
|       9 | 0x2CEF      |       11503 |

## String References

- **11502**: I can feel them... Can't you feel them? They're all around us. Breathing down our necks. Scratching at our doors. It's only a matter of time before they...
- **11503**: You had better get ready, for if you don't, you could be their next...victim!
- **11504**: I can't feel them... I can't feel their presence anymore! You must have succeeded in sending one back into the hell from which it spawned forth.
- **11505**: But I sense that it won't be long before the beast rears its head once more. It might be as soon as ( Earth time)!
- **11506**: I can feel them... They're close, and getting closer! You're an adventurer, right? You know what I'm talking about--those "things" up on Cape Riverne.
- **11507**: If we don't do something now, there's no telling what terrible fate awaits us. I'd go myself, but I have a bad case of bunions on my left foot.
- **11508**: Oh, if I could only use this artifact to call forth the terrible beasts from their grottoes. Then I could vanquish them and free Tavnazia--no, Vana'diel--from the doom that lurks in the darkness!
- **11509**: Where did I obtain this rare item, you ask? It was not but a few days ago that a strange merchant from the Far East visited the safehold. When he said he was selling magical items that could be used in defeating wretched wyrms and deadly dragons, I sold most of my belongings and purchased all he had.
- **11510**: Here, why don't you take one? No, I don't need any reimbursement. Just knowing that a brave, strong adventurer such as yourself now has the ability to become the savior of mankind gives me peace of mind.
- **11511**: But be forewarned. The wrath of the monsters that dwell on the cape will not easily be quelled. Take care in your journey, and if you ever need another one of these artifacts, do not hesitate to ask!

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

### Event 520

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11511*)
    → "But be forewarned. The wrath of the monsters that dwell on the cape will not easily be quelled. Take care in your journey, and if you ever need another one of these artifacts, do not hesitate to ask!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 521

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 28 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      42 1E F0 FF              B...
0010: FF 7F 1D 01 80 23 1D 02  80 23 1D 03 80 23 1D 04  .....#...#...#..
0020: 80 23 1D 05 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x000C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=11506*)
    → "I can feel them... They're close, and getting closer! You're an adventurer, right? You know what I'm talking about--those "things" up on Cape Riverne."
  3: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=11507*)
    → "If we don't do something now, there's no telling what terrible fate awaits us. I'd go myself, but I have a bad case of bunions on my left foot."
  5: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=11508*)
    → "Oh, if I could only use this artifact to call forth the terrible beasts from their grottoes. Then I could vanquish them and free Tavnazia--no, Vana'diel--from the doom that lurks in the darkness!"
  7: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=11509*)
    → "Where did I obtain this rare item, you ask? It was not but a few days ago that a strange merchant from the Far East visited the safehold. When he said he was selling magical items that could be used in defeating wretched wyrms and deadly dragons, I sold most of my belongings and purchased all he had."
  9: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=11510*)
    → "Here, why don't you take one? No, I don't need any reimbursement. Just knowing that a brave, strong adventurer such as yourself now has the ability to become the savior of mankind gives me peace of mind."
 11: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0026 [0x21] END_EVENT
 13: 0x0027 [0x00] END_REQSTACK()
```

### Event 522

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1E F0 FF FF 7F 1D 06 80          ........
0030: 23 1D 07 80 23 21 00                              #...#!.         
```

#### Opcodes

```
  0: 0x0028 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=11504*)
    → "I can't feel them... I can't feel their presence anymore! You must have succeeded in sending one back into the hell from which it spawned forth."
  2: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=11505*)
    → "But I sense that it won't be long before the beast rears its head once more. It might be as soon as ( Earth time)!"
  4: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0035 [0x21] END_EVENT
  6: 0x0036 [0x00] END_REQSTACK()
```

### Event 523

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1E  F0 FF FF 7F 1D 08 80 23         ........#
0040: 1D 09 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0037 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=11502*)
    → "I can feel them... Can't you feel them? They're all around us. Breathing down our necks. Scratching at our doors. It's only a matter of time before they..."
  2: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=11503*)
    → "You had better get ready, for if you don't, you could be their next...victim!"
  4: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0044 [0x21] END_EVENT
  6: 0x0045 [0x00] END_REQSTACK()
```
