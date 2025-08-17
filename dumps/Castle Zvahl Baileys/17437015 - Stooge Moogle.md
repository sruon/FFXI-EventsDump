# 17437015 - Stooge Moogle

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Castle Zvahl Baileys (ID: 161) |
| Block Size       | 224 bytes                      |
| Total Events     | 5                              |
| References Count | 13                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |     10 |              2 |
| [100](#event-100)     | 0x000A       |      1 |              1 |
| [101](#event-101)     | 0x000B       |      1 |              1 |
| [102](#event-102)     | 0x000C       |    108 |             21 |
| [103](#event-103)     | 0x0078       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x5B570     |      374128 |
|       2 | 0xFFFFC55E  |  4294952286 |
|       3 | 0xFFFFD0BE  |  4294955198 |
|       4 | 0x0DCA      |        3530 |
|       5 | 0xFFFDA2F3  |  4294812403 |
|       6 | 0x420C      |       16908 |
|       7 | 0xFFFFA241  |  4294943297 |
|       8 | 0x0379      |         889 |
|       9 | 0x0014      |          20 |
|      10 | 0x0080      |         128 |
|      11 | 0x005A      |          90 |
|      12 | 0x002D      |          45 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 6C 57 11 0A 01 00 80 00  80 00                    lW........      
```

#### Opcodes

```
  0: 0x0000 [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17437015/0x010A1157), end_alpha=0*, fade_time=0*)
  1: 0x0009 [0x00] END_REQSTACK()
```

### Event 100

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                00                           .     
```

#### Opcodes

```
  0: 0x000A [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   00                         .    
```

#### Opcodes

```
  0: 0x000B [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000C    |
| Data Size    | 108 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      02 02 10 00              ....
0010: 80 00 2B 00 03 00 00 01  80 03 01 00 02 80 03 02  ..+.............
0020: 00 03 80 03 03 00 04 80  01 3F 00 03 00 00 05 80  .........?......
0030: 03 01 00 06 80 03 02 00  07 80 03 03 00 08 80 37  ...............7
0040: 00 00 01 00 02 00 03 00  2F 00 57 11 0A 01 4A 57  ......../.W...JW
0050: 11 0A 01 F0 FF FF 7F 4E  00 57 11 0A 01 1C 09 80  .......N.W......
0060: 4A F0 FF FF 7F 57 11 0A  01 6F 70 6C 57 11 0A 01  J....W...oplW...
0070: 0A 80 0B 80 1C 0C 80 00                           ........        
```

#### Opcodes

```
  0: 0x000C [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x002B
  1: 0x0014 [0x03] ExtData[1]->WorkLocal[0] = 374128*
  2: 0x0019 [0x03] ExtData[1]->WorkLocal[1] = 4294952286*
  3: 0x001E [0x03] ExtData[1]->WorkLocal[2] = 4294955198*
  4: 0x0023 [0x03] ExtData[1]->WorkLocal[3] = 3530*
  5: 0x0028 [0x01] GOTO 0x003F
  6: 0x002B [0x03] ExtData[1]->WorkLocal[0] = 4294812403*
  7: 0x0030 [0x03] ExtData[1]->WorkLocal[1] = 16908*
  8: 0x0035 [0x03] ExtData[1]->WorkLocal[2] = 4294943297*
  9: 0x003A [0x03] ExtData[1]->WorkLocal[3] = 889*

SUBROUTINE_003F:
 10: 0x003F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
 11: 0x0048 [0x2F] Stooge Moogle (ID: 17437015/0x010A1157)->Render.Flags0 &= ~0x80000 // Bit 19
 12: 0x004E [0x4A] Stooge Moogle (ID: 17437015/0x010A1157) looks at LocalPlayer
 13: 0x0057 [0x4E] SET_ENTITY_HIDE_FLAG: Show Stooge Moogle (ID: 17437015/0x010A1157)
 14: 0x005D [0x1C] WAIT(20* ticks)
 15: 0x0060 [0x4A] LocalPlayer looks at Stooge Moogle (ID: 17437015/0x010A1157)
 16: 0x0069 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 17: 0x006A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 18: 0x006B [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17437015/0x010A1157), end_alpha=128*, fade_time=90*)
 19: 0x0074 [0x1C] WAIT(45* ticks)
 20: 0x0077 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          6C 57 11 0A 01 00 80 0B          lW......
0080: 80 1C 0B 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0078 [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17437015/0x010A1157), end_alpha=0*, fade_time=90*)
  1: 0x0081 [0x1C] WAIT(90* ticks)
  2: 0x0084 [0x00] END_REQSTACK()
```
