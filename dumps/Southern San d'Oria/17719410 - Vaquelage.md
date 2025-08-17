# 17719410 - Vaquelage

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 584 bytes                     |
| Total Events     | 13                            |
| References Count | 36                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [672](#event-672)        | 0x0001       |     76 |             18 |
| [945](#event-945)        | 0x004D       |     10 |              2 |
| [65535.1](#event-655351) | 0x0057       |     15 |              5 |
| [65535.2](#event-655352) | 0x0066       |     68 |             12 |
| [65535.3](#event-655353) | 0x00AA       |     45 |              9 |
| [65535.4](#event-655354) | 0x00D7       |     89 |             16 |
| [65535.5](#event-655355) | 0x0130       |     15 |              5 |
| [65535.6](#event-655356) | 0x013F       |     10 |              2 |
| [65535.7](#event-655357) | 0x0149       |     15 |              5 |
| [65535.8](#event-655358) | 0x0158       |     18 |              6 |
| [3506](#event-3506)      | 0x016A       |      4 |              2 |
| [3507](#event-3507)      | 0x016E       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2100      |        8448 |
|       2 | 0x20FF      |        8447 |
|       3 | 0x0000      |           0 |
|       4 | 0x0001      |           1 |
|       5 | 0x40000000  |  1073741824 |
|       6 | 0x001E      |          30 |
|       7 | 0x0060      |          96 |
|       8 | 0x000B      |          11 |
|       9 | 0xF906      |       63750 |
|      10 | 0xFFFFC4F8  |  4294952184 |
|      11 | 0x07CF      |        1999 |
|      12 | 0x0013      |          19 |
|      13 | 0x7FC6      |       32710 |
|      14 | 0xFFFF82CC  |  4294935244 |
|      15 | 0x004B      |          75 |
|      16 | 0x0027      |          39 |
|      17 | 0x4B65      |       19301 |
|      18 | 0xFFFF927C  |  4294939260 |
|      19 | 0x001D      |          29 |
|      20 | 0x000D      |          13 |
|      21 | 0xFFFFE0FB  |  4294959355 |
|      22 | 0xFFFFFCD8  |  4294966488 |
|      23 | 0x0078      |         120 |
|      24 | 0xFFFFBEF4  |  4294950644 |
|      25 | 0xFFFFD7DD  |  4294957021 |
|      26 | 0xFFFFDD9F  |  4294958495 |
|      27 | 0xFFFFA44E  |  4294943822 |
|      28 | 0x007F      |         127 |
|      29 | 0x0028      |          40 |
|      30 | 0x3192      |       12690 |
|      31 | 0xFFFFCF7D  |  4294954877 |
|      32 | 0x0025      |          37 |
|      33 | 0x2E04      |       11780 |
|      34 | 0xFFFFCBDF  |  4294953951 |
|      35 | 0x0BA3      |        2979 |

## String References

- **8447**: Send an item? [Send something./No, thanks.]
- **8448**: Parcels delivered to rooms anywhere in Vana'diel!

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

### Event 672

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 76 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0020: 24 02 80 03 80 03 80 25  02 00 10 03 80 00 38 00  $......%......8.
0030: 03 01 10 03 80 01 48 00  02 00 10 04 80 00 48 00  ......H.......H.
0040: 03 01 10 05 80 01 48 00  1C 06 80 21 00           ......H....!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8448*)
    → "Parcels delivered to rooms anywhere in Vana'diel!"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0020 [0x24] CREATE_DIALOG(message_id=8447*, default_option=0*, option_flags=0*)
    → "Send an item? [Send something./No, thanks.]"
  8: 0x0027 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0028 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0038
 10: 0x0030 [0x03] Work_Zone[1] = 0*
 11: 0x0035 [0x01] GOTO 0x0048
 12: 0x0038 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0048
 13: 0x0040 [0x03] Work_Zone[1] = 1073741824*
 14: 0x0045 [0x01] GOTO 0x0048

SUBROUTINE_0048:
 15: 0x0048 [0x1C] WAIT(30* ticks)
 16: 0x004B [0x21] END_EVENT
 17: 0x004C [0x00] END_REQSTACK()
```

### Event 945

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         6C F8 FF               l..
0050: FF 7F 07 80 04 80 00                              .......         
```

#### Opcodes

```
  0: 0x004D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=96*, fade_time=1*)
  1: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  08 80 1F 00 09 80 0A 80         2........
0060: 0B 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=63.750*, Z=-15.112*, Y=1.999*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 68 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   32 0C  80 1F 00 0D 80 0E 80 0B        2.........
0070: 80 1F 01 6F 1E 3D 60 0E  01 6F 76 F8 FF FF 7F 4A  ...o.=`..ov....J
0080: 3D 60 0E 01 F8 FF FF 7F  5B 0F 80 F8 FF FF 7F F8  =`......[.......
0090: FF FF 7F 74 6C 6B 30 1C  06 80 5B 0F 80 3D 60 0E  ...tlk0...[..=`.
00A0: 01 3D 60 0E 01 74 68 6B  30 00                    .=`..thk0.      
```

#### Opcodes

```
  0: 0x0066 [0x32] ExtData[1]->MainSpeed = 19* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=32.710*, Z=-32.052*, Y=1.999*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0074 [0x1E] EventEntity looks at Authere (ID: 17719357/0x010E603D) and starts talking
  5: 0x0079 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x007A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x007F [0x4A] Authere (ID: 17719357/0x010E603D) looks at EventEntity
  8: 0x0088 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  9: 0x0097 [0x1C] WAIT(30* ticks)
 10: 0x009A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [Authere (ID: 17719357/0x010E603D), Authere (ID: 17719357/0x010E603D)], work=75*
 11: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                32 10 80 1F 00 11            2.....
00B0: 80 12 80 0B 80 1F 01 6F  4A 72 60 0E 01 F8 FF FF  .......oJr`.....
00C0: 7F 6F 76 72 60 0E 01 66  13 80 72 60 0E 01 72 60  .ovr`..f..r`..r`
00D0: 0E 01 74 77 61 30 00                              ..twa0.         
```

#### Opcodes

```
  0: 0x00AA [0x32] ExtData[1]->MainSpeed = 39* * 0.1
  1: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=19.301*, Z=-28.036*, Y=1.999*
  2: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B8 [0x4A] Vaquelage (ID: 17719410/0x010E6072) looks at EventEntity
  5: 0x00C1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00C2 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Vaquelage (ID: 17719410/0x010E6072) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x00C7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [Vaquelage (ID: 17719410/0x010E6072), Vaquelage (ID: 17719410/0x010E6072)], work=29*
  8: 0x00D6 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 89 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      32  14 80 1F 00 15 80 16 80         2........
00E0: 0B 80 1F 01 6F 79 00 F8  FF FF 7F 7E 60 0E 01 4A  ....oy.....~`..J
00F0: 7E 60 0E 01 F8 FF FF 7F  6F 76 7E 60 0E 01 5B 10  ~`......ov~`..[.
0100: 80 7E 60 0E 01 7E 60 0E  01 74 6C 6B 30 1C 17 80  .~`..~`..tlk0...
0110: 5B 10 80 7E 60 0E 01 7E  60 0E 01 74 6C 6B 31 7B  [..~`..~`..tlk1{
0120: F8 FF FF 7F 1F 00 18 80  19 80 0B 80 1F 01 6F 00  ..............o.
```

#### Opcodes

```
  0: 0x00D7 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00DA [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.941*, Z=-0.808*, Y=1.999*
  2: 0x00E2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00E5 [0x79] EventEntity looks at Ailevia (ID: 17719422/0x010E607E) (Basic look)
  5: 0x00EF [0x4A] Ailevia (ID: 17719422/0x010E607E) looks at EventEntity
  6: 0x00F8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00F9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ailevia (ID: 17719422/0x010E607E) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00FE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Ailevia (ID: 17719422/0x010E607E), Ailevia (ID: 17719422/0x010E607E)], work=39*
  9: 0x010D [0x1C] WAIT(120* ticks)
 10: 0x0110 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Ailevia (ID: 17719422/0x010E607E), Ailevia (ID: 17719422/0x010E607E)], work=39*
 11: 0x011F [0x7B] EventEntity stops talking
 12: 0x0124 [0x1F] MOVE_ENTITY: EventEntity moves to X=-16.652*, Z=-10.275*, Y=1.999*
 13: 0x012C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x012E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 32 08 80 1F 00 1A 80 1B  80 0B 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0130 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0133 [0x1F] MOVE_ENTITY: EventEntity moves to X=-8.801*, Z=-23.474*, Y=1.999*
  2: 0x013B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x013D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x013E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               6C                 l
0140: F8 FF FF 7F 1C 80 04 80  00                       .........       
```

#### Opcodes

```
  0: 0x013F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=1*)
  1: 0x0148 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0149   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             32 1D 80 1F 00 1E 80           2......
0150: 1F 80 0B 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0149 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x014C [0x1F] MOVE_ENTITY: EventEntity moves to X=12.690*, Z=-12.419*, Y=1.999*
  2: 0x0154 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0156 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0157 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0158   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          1C 06 80 32 20 80 1F 00          ...2 ...
0160: 21 80 22 80 0B 80 1F 01  6F 00                    !.".....o.      
```

#### Opcodes

```
  0: 0x0158 [0x1C] WAIT(30* ticks)
  1: 0x015B [0x32] ExtData[1]->MainSpeed = 37* * 0.1
  2: 0x015E [0x1F] MOVE_ENTITY: EventEntity moves to X=11.780*, Z=-13.345*, Y=1.999*
  3: 0x0166 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0168 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0169 [0x00] END_REQSTACK()
```

### Event 3506

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016A  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                39 23 80 00                  9#..  
```

#### Opcodes

```
  0: 0x016A [0x39] SET_ENTITY_DIRECTION(direction=16.4°*)
  1: 0x016D [0x00] END_REQSTACK()
```

### Event 3507

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016E  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                            39 23                9#
0170: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x016E [0x39] SET_ENTITY_DIRECTION(direction=16.4°*)
  1: 0x0171 [0x00] END_REQSTACK()
```
