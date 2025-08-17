# 17756221 - Six of Diamonds

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 76 bytes                 |
| Total Events     | 3                        |
| References Count | 3                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [265](#event-265)     | 0x0001       |     26 |             11 |
| [443](#event-443)     | 0x001B       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E16      |        7702 |
|       1 | 0x0258      |         600 |
|       2 | 0x1E17      |        7703 |

## String References

- **7702**: tHIs$26dIs-TrIcT$26CaL-LeD$26wInDuRsT WaLlS!$26SiX$26iS$26CArDIan! prO-tEcTs$26WiNdUrSt!
- **7703**: WIndUrst$26wOOds bEyOnd$26thAt$26ArchwAy! mAnY$26mIthrA$26lIvE thErE!

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

### Event 265

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 4B 3D F0 0E   .....op...#K=..
0010: 01 01 80 1D 02 80 23 20  00 21 00                 ......# .!.     
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7702*)
    → "tHIs$26dIs-TrIcT$26CaL-LeD$26wInDuRsT WaLlS!$26SiX$26iS$26CArDIan! prO-tEcTs$26WiNdUrSt!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x4B] UPDATE_ENTITY_YAW(entity=Six of Diamonds (ID: 17756221/0x010EF03D), yaw=3.3°*)
  6: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=7703*)
    → "WIndUrst$26wOOds bEyOnd$26thAt$26ArchwAy! mAnY$26mIthrA$26lIvE thErE!"
  7: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0017 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0019 [0x21] END_EVENT
 10: 0x001A [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   92 01 F8 FF FF             .....
0020: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x001B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0021 [0x00] END_REQSTACK()
```
