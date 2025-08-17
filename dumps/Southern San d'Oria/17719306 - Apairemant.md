# 17719306 - Apairemant

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 472 bytes                     |
| Total Events     | 12                            |
| References Count | 30                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [945](#event-945)        | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [65535.2](#event-655352) | 0x001A       |     68 |             12 |
| [65535.3](#event-655353) | 0x005E       |     45 |              9 |
| [65535.4](#event-655354) | 0x008B       |     89 |             16 |
| [65535.5](#event-655355) | 0x00E4       |     15 |              5 |
| [65535.6](#event-655356) | 0x00F3       |     10 |              2 |
| [65535.7](#event-655357) | 0x00FD       |     15 |              5 |
| [65535.8](#event-655358) | 0x010C       |     18 |              6 |
| [3506](#event-3506)      | 0x011E       |      1 |              1 |
| [3507](#event-3507)      | 0x011F       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0060      |          96 |
|       1 | 0x0001      |           1 |
|       2 | 0x000B      |          11 |
|       3 | 0xF906      |       63750 |
|       4 | 0xFFFFC4F8  |  4294952184 |
|       5 | 0x07CF      |        1999 |
|       6 | 0x0013      |          19 |
|       7 | 0x7FC6      |       32710 |
|       8 | 0xFFFF82CC  |  4294935244 |
|       9 | 0x004B      |          75 |
|      10 | 0x001E      |          30 |
|      11 | 0x0027      |          39 |
|      12 | 0x4B65      |       19301 |
|      13 | 0xFFFF927C  |  4294939260 |
|      14 | 0x001D      |          29 |
|      15 | 0x000D      |          13 |
|      16 | 0xFFFFE0FB  |  4294959355 |
|      17 | 0xFFFFFCD8  |  4294966488 |
|      18 | 0x0078      |         120 |
|      19 | 0xFFFFBEF4  |  4294950644 |
|      20 | 0xFFFFD7DD  |  4294957021 |
|      21 | 0xFFFFDD9F  |  4294958495 |
|      22 | 0xFFFFA44E  |  4294943822 |
|      23 | 0x007F      |         127 |
|      24 | 0x0028      |          40 |
|      25 | 0x3192      |       12690 |
|      26 | 0xFFFFCF7D  |  4294954877 |
|      27 | 0x0025      |          37 |
|      28 | 0x2E04      |       11780 |
|      29 | 0xFFFFCBDF  |  4294953951 |

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

### Event 945

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6C F8 FF FF 7F 00 80  01 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0001 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=96*, fade_time=1*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 02 80 1F 00             2....
0010: 03 80 04 80 05 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=63.750*, Z=-15.112*, Y=1.999*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 68 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 06 80 1F 00 07            2.....
0020: 80 08 80 05 80 1F 01 6F  1E 3D 60 0E 01 6F 76 F8  .......o.=`..ov.
0030: FF FF 7F 4A 3D 60 0E 01  F8 FF FF 7F 5B 09 80 F8  ...J=`......[...
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1C 0A 80 5B 09  .......tlk0...[.
0050: 80 3D 60 0E 01 3D 60 0E  01 74 68 6B 30 00        .=`..=`..thk0.  
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 19* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=32.710*, Z=-32.052*, Y=1.999*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0028 [0x1E] EventEntity looks at Authere (ID: 17719357/0x010E603D) and starts talking
  5: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x002E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0033 [0x4A] Authere (ID: 17719357/0x010E603D) looks at EventEntity
  8: 0x003C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  9: 0x004B [0x1C] WAIT(30* ticks)
 10: 0x004E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [Authere (ID: 17719357/0x010E603D), Authere (ID: 17719357/0x010E603D)], work=75*
 11: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 0B                2.
0060: 80 1F 00 0C 80 0D 80 05  80 1F 01 6F 4A 72 60 0E  ...........oJr`.
0070: 01 F8 FF FF 7F 6F 76 72  60 0E 01 66 0E 80 72 60  .....ovr`..f..r`
0080: 0E 01 72 60 0E 01 74 77  61 30 00                 ..r`..twa0.     
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 39* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.301*, Z=-28.036*, Y=1.999*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006C [0x4A] Vaquelage (ID: 17719410/0x010E6072) looks at EventEntity
  5: 0x0075 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0076 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Vaquelage (ID: 17719410/0x010E6072) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [Vaquelage (ID: 17719410/0x010E6072), Vaquelage (ID: 17719410/0x010E6072)], work=29*
  8: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 89 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   32 0F 80 1F 00             2....
0090: 10 80 11 80 05 80 1F 01  6F 79 00 F8 FF FF 7F 7E  ........oy.....~
00A0: 60 0E 01 4A 7E 60 0E 01  F8 FF FF 7F 6F 76 7E 60  `..J~`......ov~`
00B0: 0E 01 5B 0B 80 7E 60 0E  01 7E 60 0E 01 74 6C 6B  ..[..~`..~`..tlk
00C0: 30 1C 12 80 5B 0B 80 7E  60 0E 01 7E 60 0E 01 74  0...[..~`..~`..t
00D0: 6C 6B 31 7B F8 FF FF 7F  1F 00 13 80 14 80 05 80  lk1{............
00E0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x008B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.941*, Z=-0.808*, Y=1.999*
  2: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0098 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0099 [0x79] EventEntity looks at Ailevia (ID: 17719422/0x010E607E) (Basic look)
  5: 0x00A3 [0x4A] Ailevia (ID: 17719422/0x010E607E) looks at EventEntity
  6: 0x00AC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00AD [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ailevia (ID: 17719422/0x010E607E) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00B2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Ailevia (ID: 17719422/0x010E607E), Ailevia (ID: 17719422/0x010E607E)], work=39*
  9: 0x00C1 [0x1C] WAIT(120* ticks)
 10: 0x00C4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Ailevia (ID: 17719422/0x010E607E), Ailevia (ID: 17719422/0x010E607E)], work=39*
 11: 0x00D3 [0x7B] EventEntity stops talking
 12: 0x00D8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-16.652*, Z=-10.275*, Y=1.999*
 13: 0x00E0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x00E2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             32 02 80 1F  00 15 80 16 80 05 80 1F      2...........
00F0: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x00E4 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x00E7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-8.801*, Z=-23.474*, Y=1.999*
  2: 0x00EF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F2 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F3   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          6C F8 FF FF 7F  17 80 01 80 00              l.........   
```

#### Opcodes

```
  0: 0x00F3 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=1*)
  1: 0x00FC [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         32 18 80               2..
0100: 1F 00 19 80 1A 80 05 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x00FD [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0100 [0x1F] MOVE_ENTITY: EventEntity moves to X=12.690*, Z=-12.419*, Y=1.999*
  2: 0x0108 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x010A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x010B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      1C 0A 80 32              ...2
0110: 1B 80 1F 00 1C 80 1D 80  05 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x010C [0x1C] WAIT(30* ticks)
  1: 0x010F [0x32] ExtData[1]->MainSpeed = 37* * 0.1
  2: 0x0112 [0x1F] MOVE_ENTITY: EventEntity moves to X=11.780*, Z=-13.345*, Y=1.999*
  3: 0x011A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x011C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x011D [0x00] END_REQSTACK()
```

### Event 3506

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            00                   . 
```

#### Opcodes

```
  0: 0x011E [0x00] END_REQSTACK()
```

### Event 3507

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               00                 .
```

#### Opcodes

```
  0: 0x011F [0x00] END_REQSTACK()
```
