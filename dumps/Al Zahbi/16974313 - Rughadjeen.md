# 16974313 - Rughadjeen

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 416 bytes         |
| Total Events     | 13                |
| References Count | 17                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [5](#event-5)            | 0x0001       |     13 |              3 |
| [6](#event-6)            | 0x000E       |     13 |              3 |
| [8](#event-8)            | 0x001B       |     13 |              3 |
| [9](#event-9)            | 0x0028       |     13 |              3 |
| [11](#event-11)          | 0x0035       |     13 |              3 |
| [12](#event-12)          | 0x0042       |     13 |              3 |
| [211](#event-211)        | 0x004F       |     39 |             14 |
| [65535.1](#event-655351) | 0x0076       |     13 |              3 |
| [265](#event-265)        | 0x0083       |     39 |             14 |
| [273](#event-273)        | 0x00AA       |     59 |             18 |
| [65535.2](#event-655352) | 0x00E5       |     10 |              2 |
| [284](#event-284)        | 0x00EF       |     39 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1E09      |        7689 |
|       2 | 0x012C      |         300 |
|       3 | 0x042B      |        1067 |
|       4 | 0x1E0A      |        7690 |
|       5 | 0x0024      |          36 |
|       6 | 0x1E0B      |        7691 |
|       7 | 0x001E      |          30 |
|       8 | 0x001A      |          26 |
|       9 | 0x1E0C      |        7692 |
|      10 | 0x1E0D      |        7693 |
|      11 | 0xFFFEDC98  |  4294892696 |
|      12 | 0x131C7     |       78279 |
|      13 | 0xFFFFE890  |  4294961296 |
|      14 | 0x0C0E      |        3086 |
|      15 | 0x1E0E      |        7694 |
|      16 | 0x1E0F      |        7695 |

## String References

- **7689**: Her Magnificence the Empress is safely shielded now, and it is all thanks to your efforts. You have the makings of a hero.
- **7690**: The mercenaries and the Imperial Army shall fight and perish as one to shield the Empress from harm!
- **7691**: May Her Magnificence reign a thousand years!
- **7692**: My presence was all for naught... My failure to protect the Astral Candescence is a transgression worthy of a thousand deaths...
- **7693**: Hear my plea... You mercenaries may be all that I can trust. Recover the Astral Candescence and bring it safely back to Al Zahbi...I implore you!
- **7694**: Ah, [/Private Second Class /Private First Class /Superior Private /Lance Corporal /Corporal /Sergeant /Sergeant Major /Chief Sergeant /Second Lieutenant /First Lieutenant /Captain ]<Player>! It is reassuring indeed to have such a mighty ally to aid in the defense of Al Zahbi.
- **7695**: I am honored to fight at your side in the name of Her Magnificence!

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

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            92 01                ..
0010: F8 FF FF 7F 94 01 F8 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x000E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0014 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x001A [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   92 01 F8 FF FF             .....
0020: 7F 94 01 F8 FF FF 7F 00                           ........        
```

#### Opcodes

```
  0: 0x001B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0021 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0027 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          92 01 F8 FF FF 7F 94 01          ........
0030: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0028 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002E [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0034 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                92 01 F8  FF FF 7F 94 01 F8 FF FF       ...........
0040: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0035 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003B [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0041 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       92 01 F8 FF FF 7F  94 01 F8 FF FF 7F 00       ............. 
```

#### Opcodes

```
  0: 0x0042 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0048 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x004E [0x00] END_REQSTACK()
```

### Event 211

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 39 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               43                 C
0050: 00 43 01 20 01 42 03 01  10 00 80 1E F0 FF FF 7F  .C. .B..........
0060: 6F 70 6E E9 01 03 01 00  80 99 E9 01 03 01 1D 01  opn.............
0070: 80 1C 02 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x004F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  1: 0x0051 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  2: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0055 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0056 [0x03] Work_Zone[1] = 1*
  5: 0x005B [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x0060 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0061 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0062 [0x6E] Rughadjeen (ID: 16974313/0x010301E9) uses emote 1*
  9: 0x0069 [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
 10: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=7689*)
    → "Her Magnificence the Empress is safely shielded now, and it is all thanks to your efforts. You have the makings of a hero."
 11: 0x0071 [0x1C] WAIT(300* ticks)
 12: 0x0074 [0x21] END_EVENT
 13: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   6E F8  FF FF 7F 03 80 99 F8 FF        n.........
0080: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0076 [0x6E] EventEntity uses emote 1067*
  1: 0x007D [0x99] Wait for EventEntity animation to complete
  2: 0x0082 [0x00] END_REQSTACK()
```

### Event 265

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0083   |
| Data Size    | 39 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          20 01 1E F0 FF  FF 7F 6F 70 1D 04 80 23      ......op...#
0090: 6E E9 01 03 01 05 80 99  E9 01 03 01 1D 06 80 23  n..............#
00A0: 99 E9 01 03 01 1C 07 80  21 00                    ........!.      
```

#### Opcodes

```
  0: 0x0083 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0085 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x008A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x008B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=7690*)
    → "The mercenaries and the Imperial Army shall fight and perish as one to shield the Empress from harm!"
  5: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0090 [0x6E] Rughadjeen (ID: 16974313/0x010301E9) uses emote 36*
  7: 0x0097 [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
  8: 0x009C [0x1D] PRINT_EVENT_MESSAGE(message_id=7691*)
    → "May Her Magnificence reign a thousand years!"
  9: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00A0 [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
 11: 0x00A5 [0x1C] WAIT(30* ticks)
 12: 0x00A8 [0x21] END_EVENT
 13: 0x00A9 [0x00] END_REQSTACK()
```

### Event 273

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 59 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                20 01 1E F0 FF FF             .....
00B0: 7F 6F 70 6E E9 01 03 01  08 80 99 E9 01 03 01 1D  .opn............
00C0: 09 80 23 99 E9 01 03 01  1C 07 80 6E E9 01 03 01  ..#........n....
00D0: 05 80 99 E9 01 03 01 1D  0A 80 23 99 E9 01 03 01  ..........#.....
00E0: 1C 07 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x00AA [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00AC [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00B2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00B3 [0x6E] Rughadjeen (ID: 16974313/0x010301E9) uses emote 26*
  5: 0x00BA [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
  6: 0x00BF [0x1D] PRINT_EVENT_MESSAGE(message_id=7692*)
    → "My presence was all for naught... My failure to protect the Astral Candescence is a transgression worthy of a thousand deaths..."
  7: 0x00C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00C3 [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
  9: 0x00C8 [0x1C] WAIT(30* ticks)
 10: 0x00CB [0x6E] Rughadjeen (ID: 16974313/0x010301E9) uses emote 36*
 11: 0x00D2 [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
 12: 0x00D7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7693*)
    → "Hear my plea... You mercenaries may be all that I can trust. Recover the Astral Candescence and bring it safely back to Al Zahbi...I implore you!"
 13: 0x00DA [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00DB [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
 15: 0x00E0 [0x1C] WAIT(30* ticks)
 16: 0x00E3 [0x21] END_EVENT
 17: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                37 0B 80  0C 80 0D 80 0E 80 00          7......... 
```

#### Opcodes

```
  0: 0x00E5 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-74.600*, z=78.279*, y=-6.000*, direction=271.2°*
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 284

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 39 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               20                  
00F0: 01 1E F0 FF FF 7F 6F 70  1D 0F 80 23 6E E9 01 03  ......op...#n...
0100: 01 05 80 99 E9 01 03 01  1D 10 80 23 99 E9 01 03  ...........#....
0110: 01 1C 07 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x00EF [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00F1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00F6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00F7 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00F8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7694*)
    → "Ah, [/Private Second Class /Private First Class /Superior Private /Lance Corporal /Corporal /Sergeant /Sergeant Major /Chief Sergeant /Second Lieutenant /First Lieutenant /Captain ]<Player>! It is reassuring indeed to have such a mighty ally to aid in the defense of Al Zahbi."
  5: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00FC [0x6E] Rughadjeen (ID: 16974313/0x010301E9) uses emote 36*
  7: 0x0103 [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
  8: 0x0108 [0x1D] PRINT_EVENT_MESSAGE(message_id=7695*)
    → "I am honored to fight at your side in the name of Her Magnificence!"
  9: 0x010B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x010C [0x99] Wait for Rughadjeen (ID: 16974313/0x010301E9) animation to complete
 11: 0x0111 [0x1C] WAIT(30* ticks)
 12: 0x0114 [0x21] END_EVENT
 13: 0x0115 [0x00] END_REQSTACK()
```
