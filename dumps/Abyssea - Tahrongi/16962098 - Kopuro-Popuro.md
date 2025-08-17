# 16962098 - Kopuro-Popuro

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 284 bytes                   |
| Total Events     | 8                           |
| References Count | 13                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [306](#event-306)     | 0x0001       |     42 |              8 |
| [307](#event-307)     | 0x002B       |     55 |             15 |
| [308](#event-308)     | 0x0062       |     13 |              7 |
| [309](#event-309)     | 0x006F       |     17 |              9 |
| [310](#event-310)     | 0x0080       |     39 |             15 |
| [311](#event-311)     | 0x00A7       |     13 |              7 |
| [312](#event-312)     | 0x00B4       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0150      |         336 |
|       1 | 0x1EAE      |        7854 |
|       2 | 0x001E      |          30 |
|       3 | 0x1EAF      |        7855 |
|       4 | 0x1EB0      |        7856 |
|       5 | 0x1EB1      |        7857 |
|       6 | 0x1EB8      |        7864 |
|       7 | 0x1EBA      |        7866 |
|       8 | 0x1EBF      |        7871 |
|       9 | 0x1EC1      |        7873 |
|      10 | 0x0800      |        2048 |
|      11 | 0x003C      |          60 |
|      12 | 0x1EC2      |        7874 |

## String References

- **7854**: My dear, beloved Boxuxu... They could postaru me here for an eternity, but with you by my side, every moment would be bliss!
- **7855**: Yes? What do you wantaru? A starfruit, you say? For Minister Apururu?
- **7856**: Why, Boxuxu would be happy to furnish you with what you desire. Wouldn't you, my dearestaru?
- **7857**: Who am I talking to, you ask? Why, my beloved Boxuxu, of course! Are you [daft, mistaru/daftaru, lady]? Do you not see her standing right beside me? Go ahead, talk to her! She won't bite!
- **7864**: That's a rarity-warity, my friend. Boxuxu must have taken a fancy to you! Perhaps she likes you even more than...<sniff>...me? Perish the thoughtaru!
- **7866**: No, I fear you'll have to work a bit harder to earn her favor.
- **7871**: Be bright and cheery-weery, and Boxuxu will surely take a fancy to you. Heaven knows we could all use a few more smiles in this dark and desolataru world...
- **7873**: Don't forgetaru to say your thank-yous, now! If there's one thing Boxuxu can't stand, it's someone who doesn't know their manners-wanners.
- **7874**: <Ahem>...Can't you see that Boxuxu and I would like a little privataru time now, hmmmmmm? Now back to Apururu with you!

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

### Event 306

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 42 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 67 6B 72 30   [..........gkr0
0010: 1D 01 80 23 53 F8 FF FF  7F F8 FF FF 7F 67 6B 72  ...#S........gkr
0020: 30 5E 69 64 6C 30 1C 02  80 21 00                 0^idl0...!.     
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gkr0" with entities [EventEntity, EventEntity], work=336*
  1: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7854*)
    → "My dear, beloved Boxuxu... They could postaru me here for an eternity, but with you by my side, every moment would be bliss!"
  2: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0014 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gkr0" with entities [EventEntity, EventEntity]
  4: 0x0021 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  5: 0x0026 [0x1C] WAIT(30* ticks)
  6: 0x0029 [0x21] END_EVENT
  7: 0x002A [0x00] END_REQSTACK()
```

### Event 307

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 55 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   42 1E F0 FF FF             B....
0030: 7F 6F 70 1D 03 80 23 5B  00 80 F8 FF FF 7F F8 FF  .op...#[........
0040: FF 7F 74 68 6B 31 1D 04  80 23 53 F8 FF FF 7F F8  ..thk1...#S.....
0050: FF FF 7F 74 68 6B 31 5E  69 64 6C 30 1D 05 80 23  ...thk1^idl0...#
0060: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x002B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0032 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=7855*)
    → "Yes? What do you wantaru? A starfruit, you say? For Minister Apururu?"
  5: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0037 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=336*
  7: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=7856*)
    → "Why, Boxuxu would be happy to furnish you with what you desire. Wouldn't you, my dearestaru?"
  8: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
 10: 0x0057 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 11: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7857*)
    → "Who am I talking to, you ask? Why, my beloved Boxuxu, of course! Are you [daft, mistaru/daftaru, lady]? Do you not see her standing right beside me? Go ahead, talk to her! She won't bite!"
 12: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0060 [0x21] END_EVENT
 14: 0x0061 [0x00] END_REQSTACK()
```

### Event 308

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       1E F0 FF FF 7F 6F  70 1D 06 80 23 21 00       .....op...#!. 
```

#### Opcodes

```
  0: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0068 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=7864*)
    → "That's a rarity-warity, my friend. Boxuxu must have taken a fancy to you! Perhaps she likes you even more than...<sniff>...me? Perish the thoughtaru!"
  4: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x006D [0x21] END_EVENT
  6: 0x006E [0x00] END_REQSTACK()
```

### Event 309

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 17 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               1E                 .
0070: F0 FF FF 7F 6F 70 1D 07  80 23 1D 08 80 23 21 00  ....op...#...#!.
```

#### Opcodes

```
  0: 0x006F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0075 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=7866*)
    → "No, I fear you'll have to work a bit harder to earn her favor."
  4: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=7871*)
    → "Be bright and cheery-weery, and Boxuxu will surely take a fancy to you. Heaven knows we could all use a few more smiles in this dark and desolataru world..."
  6: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x007E [0x21] END_EVENT
  8: 0x007F [0x00] END_REQSTACK()
```

### Event 310

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 39 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 1E F0 FF FF 7F 6F 70 1D  09 80 23 03 00 00 03 7F  .....op...#.....
0090: 07 00 00 0A 80 4B F8 FF  FF 7F 00 00 6F 70 1C 0B  .....K......op..
00A0: 80 1D 0C 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0080 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0085 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0086 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=7873*)
    → "Don't forgetaru to say your thank-yous, now! If there's one thing Boxuxu can't stand, it's someone who doesn't know their manners-wanners."
  4: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x008B [0x03] ExtData[1]->WorkLocal[0] = enDirCli(ExtData[1]->EventDir[1]) * 4096.0 * 0.15915963
  6: 0x0090 [0x07] ExtData[1]->WorkLocal[0] += 2048*
  7: 0x0095 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=ExtData[1]->WorkLocal[0])
  8: 0x009C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x009D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x009E [0x1C] WAIT(60* ticks)
 11: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7874*)
    → "<Ahem>...Can't you see that Boxuxu and I would like a little privataru time now, hmmmmmm? Now back to Apururu with you!"
 12: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00A5 [0x21] END_EVENT
 14: 0x00A6 [0x00] END_REQSTACK()
```

### Event 311

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      1E  F0 FF FF 7F 6F 70 1D 0C         .....op..
00B0: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x00A7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00AC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00AD [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00AE [0x1D] PRINT_EVENT_MESSAGE(message_id=7874*)
    → "<Ahem>...Can't you see that Boxuxu and I would like a little privataru time now, hmmmmmm? Now back to Apururu with you!"
  4: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00B2 [0x21] END_EVENT
  6: 0x00B3 [0x00] END_REQSTACK()
```

### Event 312

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             00                                        .           
```

#### Opcodes

```
  0: 0x00B4 [0x00] END_REQSTACK()
```
