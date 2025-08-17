# 17391850 - Courisaille

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Monastic Cavern (ID: 150) |
| Block Size       | 204 bytes                 |
| Total Events     | 4                         |
| References Count | 16                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     79 |             12 |
| [65535.2](#event-655352) | 0x0051       |     27 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0x0280      |         640 |
|       2 | 0x0043      |          67 |
|       3 | 0x0000      |           0 |
|       4 | 0x0005      |           5 |
|       5 | 0x0015      |          21 |
|       6 | 0x0087      |         135 |
|       7 | 0x179D1     |       96721 |
|       8 | 0x541C      |       21532 |
|       9 | 0xFFFFA21B  |  4294943259 |
|      10 | 0x0804      |        2052 |
|      11 | 0x0001      |           1 |
|      12 | 0x0007      |           7 |
|      13 | 0x16F51     |       94033 |
|      14 | 0x532D      |       21293 |
|      15 | 0xFFFFA227  |  4294943271 |

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

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 79 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1C 00 80 7B EA 60  09 01 4B EA 60 09 01 01    ...{.`..K.`...
0010: 80 45 02 80 F0 FF FF 7F  F0 FF FF 7F 73 67 31 32  .E..........sg12
0020: 03 80 6F 70 1C 04 80 66  05 80 EA 60 09 01 EA 60  ..op...f...`...`
0030: 09 01 73 6C 30 30 53 EA  60 09 01 EA 60 09 01 73  ..sl00S.`...`..s
0040: 6C 30 30 1C 06 80 79 00  EA 60 09 01 E9 60 09 01  l00...y..`...`..
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x1C] WAIT(15* ticks)
  1: 0x0005 [0x7B] Courisaille (ID: 17391850/0x010960EA) stops talking
  2: 0x000A [0x4B] UPDATE_ENTITY_YAW(entity=Courisaille (ID: 17391850/0x010960EA), yaw=3.5°*)
  3: 0x0011 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg12" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
  4: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0023 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0024 [0x1C] WAIT(5* ticks)
  7: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sl00" with entities [Courisaille (ID: 17391850/0x010960EA), Courisaille (ID: 17391850/0x010960EA)], work=21*
  8: 0x0036 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [Courisaille (ID: 17391850/0x010960EA), Courisaille (ID: 17391850/0x010960EA)]
  9: 0x0043 [0x1C] WAIT(135* ticks)
 10: 0x0046 [0x79] Courisaille (ID: 17391850/0x010960EA) looks at Francmage (ID: 17391849/0x010960E9) (Basic look)
 11: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    37 07 80 08 80 09 80  0A 80 1C 0B 80 32 0C 80   7...........2..
0060: 1F 00 0D 80 0E 80 0F 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x0051 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=96.721*, z=21.532*, y=-24.037*, direction=180.3°*
  1: 0x005A [0x1C] WAIT(1* ticks)
  2: 0x005D [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  3: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=94.033*, Z=21.293*, Y=-24.025*
  4: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x006B [0x00] END_REQSTACK()
```
