# 17768469 - Urubero-Mohbero

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 440 bytes               |
| Total Events     | 24                      |
| References Count | 12                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [65535.4](#event-655354) | 0x0030       |     16 |              2 |
| [65535.5](#event-655355) | 0x0040       |     14 |              2 |
| [65535.6](#event-655356) | 0x004E       |     16 |              2 |
| [65535.7](#event-655357) | 0x005E       |     14 |              2 |
| [252](#event-252)        | 0x006C       |     33 |             12 |
| [256](#event-256)        | 0x008D       |     47 |             14 |
| [99](#event-99)          | 0x00BC       |     33 |             12 |
| [236](#event-236)        | 0x00DD       |     47 |             14 |
| [429](#event-429)        | 0x010C       |      1 |              1 |
| [430](#event-430)        | 0x010D       |      1 |              1 |
| [435](#event-435)        | 0x010E       |      1 |              1 |
| [439](#event-439)        | 0x010F       |      1 |              1 |
| [440](#event-440)        | 0x0110       |      1 |              1 |
| [441](#event-441)        | 0x0111       |      1 |              1 |
| [448](#event-448)        | 0x0112       |      1 |              1 |
| [449](#event-449)        | 0x0113       |      1 |              1 |
| [454](#event-454)        | 0x0114       |      1 |              1 |
| [455](#event-455)        | 0x0115       |      1 |              1 |
| [460](#event-460)        | 0x0116       |      1 |              1 |
| [462](#event-462)        | 0x0117       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x002A      |          42 |
|       4 | 0x0232      |         562 |
|       5 | 0x0233      |         563 |
|       6 | 0x023A      |         570 |
|       7 | 0x023B      |         571 |
|       8 | 0x0085      |         133 |
|       9 | 0x0086      |         134 |
|      10 | 0x020D      |         525 |
|      11 | 0x020E      |         526 |

## String References

- **133**: You will face many new hahdy-hahdships in zose fah-away lands.
- **134**: Vhen you feel like you just can't take it anymore, remember how you gaht zis far, and sings might naht seem as bad as you sink zey ahre.
- **525**: Kupipi looks strangey-vangey. I vonder vaht's wrong? Maybe she's gaht a tumor!
- **526**: Now zat you mention it, I sah her drinking some fahnny juice this morning.
- **562**: You vant to see zee Stah Sibyl? Try bahck in a million ears.
- **563**: Zee Stah Sibyl is zee reincahnate of zee Dahn Gahddess. With zee will of zee heavens, she rules zee land. You must pay her respect!
- **570**: You vant to see zee Stah Sibyl? Try coming back in a million ears.
- **571**: Vaht iz zis you say? You ahlready met her? Zis is naht pahssible-vahssible!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 66 02 80 F8 FF FF 7F F8  FF FF 7F 73 68 6B 30 00  f..........shk0.
```

#### Opcodes

```
  0: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 53 F8 FF FF 7F F8 FF FF  7F 73 68 6B 30 00        S........shk0.  
```

#### Opcodes

```
  0: 0x0040 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [EventEntity, EventEntity]
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            66 03                f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 62 69 6B 30 00        .........bik0.  
```

#### Opcodes

```
  0: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            53 F8                S.
0060: FF FF 7F F8 FF FF 7F 62  69 6B 30 00              .......bik0.    
```

#### Opcodes

```
  0: 0x005E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x006B [0x00] END_REQSTACK()
```

### Event 252

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      1E F0 FF FF              ....
0070: 7F 6F 70 29 08 15 20 0F  01 01 1D 04 80 23 1D 05  .op).. ......#..
0080: 80 23 29 08 15 20 0F 01  03 20 00 21 00           .#).. ... .!.   
```

#### Opcodes

```
  0: 0x006C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0072 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0073 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x01)
  4: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=562*)
    → "You vant to see zee Stah Sibyl? Try bahck in a million ears."
  5: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=563*)
    → "Zee Stah Sibyl is zee reincahnate of zee Dahn Gahddess. With zee will of zee heavens, she rules zee land. You must pay her respect!"
  7: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0082 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x03)
  9: 0x0089 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x008B [0x21] END_EVENT
 11: 0x008C [0x00] END_REQSTACK()
```

### Event 256

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         1E F0 FF               ...
0090: FF 7F 6F 70 29 08 15 20  0F 01 01 1D 06 80 23 29  ..op).. ......#)
00A0: 08 15 20 0F 01 03 29 08  15 20 0F 01 04 1D 07 80  .. ...).. ......
00B0: 23 29 08 15 20 0F 01 05  20 00 21 00              #).. ... .!.    
```

#### Opcodes

```
  0: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0092 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0093 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0094 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x01)
  4: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=570*)
    → "You vant to see zee Stah Sibyl? Try coming back in a million ears."
  5: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x009F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x03)
  7: 0x00A6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x04)
  8: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=571*)
    → "Vaht iz zis you say? You ahlready met her? Zis is naht pahssible-vahssible!"
  9: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00B1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x05)
 11: 0x00B8 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x00BA [0x21] END_EVENT
 13: 0x00BB [0x00] END_REQSTACK()
```

### Event 99

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      1E F0 FF FF              ....
00C0: 7F 6F 70 29 08 15 20 0F  01 01 1D 08 80 23 1D 09  .op).. ......#..
00D0: 80 23 29 08 15 20 0F 01  03 20 00 21 00           .#).. ... .!.   
```

#### Opcodes

```
  0: 0x00BC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x01)
  4: 0x00CA [0x1D] PRINT_EVENT_MESSAGE(message_id=133*)
    → "You will face many new hahdy-hahdships in zose fah-away lands."
  5: 0x00CD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=134*)
    → "Vhen you feel like you just can't take it anymore, remember how you gaht zis far, and sings might naht seem as bad as you sink zey ahre."
  7: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00D2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x03)
  9: 0x00D9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00DB [0x21] END_EVENT
 11: 0x00DC [0x00] END_REQSTACK()
```

### Event 236

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         1E F0 FF               ...
00E0: FF 7F 6F 70 29 08 15 20  0F 01 01 1D 0A 80 23 29  ..op).. ......#)
00F0: 08 15 20 0F 01 02 29 08  15 20 0F 01 04 1D 0B 80  .. ...).. ......
0100: 23 29 08 15 20 0F 01 05  20 00 21 00              #).. ... .!.    
```

#### Opcodes

```
  0: 0x00DD [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00E2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00E3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00E4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x01)
  4: 0x00EB [0x1D] PRINT_EVENT_MESSAGE(message_id=525*)
    → "Kupipi looks strangey-vangey. I vonder vaht's wrong? Maybe she's gaht a tumor!"
  5: 0x00EE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00EF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x02)
  7: 0x00F6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x04)
  8: 0x00FD [0x1D] PRINT_EVENT_MESSAGE(message_id=526*)
    → "Now zat you mention it, I sah her drinking some fahnny juice this morning."
  9: 0x0100 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0101 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Urubero-Mohbero (ID: 17768469/0x010F2015), tag_num=0x05)
 11: 0x0108 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x010A [0x21] END_EVENT
 13: 0x010B [0x00] END_REQSTACK()
```

### Event 429

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      00                       .   
```

#### Opcodes

```
  0: 0x010C [0x00] END_REQSTACK()
```

### Event 430

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         00                     .  
```

#### Opcodes

```
  0: 0x010D [0x00] END_REQSTACK()
```

### Event 435

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                            00                   . 
```

#### Opcodes

```
  0: 0x010E [0x00] END_REQSTACK()
```

### Event 439

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               00                 .
```

#### Opcodes

```
  0: 0x010F [0x00] END_REQSTACK()
```

### Event 440

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0110  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0110 [0x00] END_REQSTACK()
```

### Event 441

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0111  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    00                                              .              
```

#### Opcodes

```
  0: 0x0111 [0x00] END_REQSTACK()
```

### Event 448

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0112  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       00                                            .             
```

#### Opcodes

```
  0: 0x0112 [0x00] END_REQSTACK()
```

### Event 449

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0113  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          00                                          .            
```

#### Opcodes

```
  0: 0x0113 [0x00] END_REQSTACK()
```

### Event 454

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0114  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             00                                        .           
```

#### Opcodes

```
  0: 0x0114 [0x00] END_REQSTACK()
```

### Event 455

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0115  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                00                                      .          
```

#### Opcodes

```
  0: 0x0115 [0x00] END_REQSTACK()
```

### Event 460

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0116  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   00                                    .         
```

#### Opcodes

```
  0: 0x0116 [0x00] END_REQSTACK()
```

### Event 462

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0117  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      00                                  .        
```

#### Opcodes

```
  0: 0x0117 [0x00] END_REQSTACK()
```
