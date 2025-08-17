# 17162742 - Kleh Engyumoh

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 188 bytes                    |
| Total Events     | 4                            |
| References Count | 9                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [431](#event-431)     | 0x0001       |     42 |             10 |
| [162](#event-162)     | 0x002B       |     73 |             13 |
| [32](#event-32)       | 0x0074       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2AB4      |       10932 |
|       2 | 0x0024      |          36 |
|       3 | 0x2AB5      |       10933 |
|       4 | 0x003B      |          59 |
|       5 | 0x2B54      |       11092 |
|       6 | 0x1170      |        4464 |
|       7 | 0x2B55      |       11093 |
|       8 | 0x2B56      |       11094 |

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

### Event 431

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0010: FF 7F 01 80 23 6E F8 FF  FF 7F 02 80 99 F8 FF FF  ....#n..........
0020: 7F 2B F8 FF FF 7F 03 80  23 21 00                 .+......#!.     
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x2B] EventEntity [10932*]:
    → "All of the mercenary leaders are combat specialists. They do it the best, do it dependably, and look good doing it! I hope I can be like one of them someday..."
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x6E] EventEntity uses emote 36*
  5: 0x001C [0x99] Wait for EventEntity animation to complete
  6: 0x0021 [0x2B] EventEntity [10933*]:
    → "If you're lucky enough, maybe you will have the opporrrtunity to fight alongside them."
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x21] END_EVENT
  9: 0x002A [0x00] END_REQSTACK()
```

### Event 162

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 73 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   4A F8 FF FF 7F             J....
0030: F0 FF FF 7F 1C 00 80 66  04 80 F8 FF FF 7F F8 FF  .......f........
0040: FF 7F 74 6C 6B 30 2B F8  FF FF 7F 05 80 23 03 02  ..tlk0+......#..
0050: 10 06 80 2B F8 FF FF 7F  07 80 23 2B F8 FF FF 7F  ...+......#+....
0060: 08 80 23 66 04 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0070: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x002B [0x4A] EventEntity looks at LocalPlayer
  1: 0x0034 [0x1C] WAIT(30* ticks)
  2: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x0046 [0x2B] EventEntity [11092*]:
    → "Oh? You're wonderrring what cuisine our honored guest from Gha Naboh might find delectable?"
  4: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004E [0x03] Work_Zone[2] = 4464*
  6: 0x0053 [0x2B] EventEntity [11093*]:
    → "Hmm, let me see... How about $0? It's something they don't have in the motherland."
  7: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x005B [0x2B] EventEntity [11094*]:
    → "You're in luck because they're in season right now and should be plump and juicy. Preparation methods differrr, but the only way to eat them is headfirst, smack-bang right down your gob!"
  9: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 11: 0x0072 [0x21] END_EVENT
 12: 0x0073 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             00                                        .           
```

#### Opcodes

```
  0: 0x0074 [0x00] END_REQSTACK()
```
