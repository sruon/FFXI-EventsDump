# 17928225 - Heroic Footprints

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Leafallia (ID: 281) |
| Block Size       | 1656 bytes          |
| Total Events     | 5                   |
| References Count | 26                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [8](#event-8)         | 0x0001       |    218 |             35 |
| [5](#event-5)         | 0x00DB       |    210 |             33 |
| [6](#event-6)         | 0x01AD       |    218 |             35 |
| [7](#event-7)         | 0x0287       |    867 |             94 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0093      |         147 |
|       1 | 0xFFFFB44B  |  4294947915 |
|       2 | 0x4439      |       17465 |
|       3 | 0xFFFFFE6D  |  4294966893 |
|       4 | 0x0B18      |        2840 |
|       5 | 0xFFFFB5BE  |  4294948286 |
|       6 | 0x51BF      |       20927 |
|       7 | 0xFFFFFDCD  |  4294966733 |
|       8 | 0x01FB      |         507 |
|       9 | 0x001E      |          30 |
|      10 | 0x0277      |         631 |
|      11 | 0x0000      |           0 |
|      12 | 0x000F      |          15 |
|      13 | 0x00C8      |         200 |
|      14 | 0x0D94      |        3476 |
|      15 | 0x1CF0      |        7408 |
|      16 | 0x1CF1      |        7409 |
|      17 | 0x0001      |           1 |
|      18 | 0x1D7A      |        7546 |
|      19 | 0x1D7B      |        7547 |
|      20 | 0x1D7C      |        7548 |
|      21 | 0x1D7D      |        7549 |
|      22 | 0x00C9      |         201 |
|      23 | 0x002D      |          45 |
|      24 | 0x0002      |           2 |
|      25 | 0x00D7      |         215 |

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

### Event 8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 218 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1A BC 03 46 01 38  00 80 2F 00 22 90 11 01   B...F.8../."...
0010: 4E 00 22 90 11 01 92 01  22 90 11 01 94 01 22 90  N.".....".....".
0020: 11 01 94 01 F0 FF FF 7F  BA 22 90 11 01 01 80 02  ........."......
0030: 80 03 80 04 80 BA F0 FF  FF 7F 05 80 06 80 07 80  ................
0040: 08 80 80 22 90 11 01 80  F0 FF FF 7F 4A 22 90 11  ..."........J"..
0050: 01 F0 FF FF 7F 4A F0 FF  FF 7F 22 90 11 01 1C 09  .....J....".....
0060: 80 45 0A 80 F0 FF FF 7F  F0 FF FF 7F 73 30 30 30  .E..........s000
0070: 0B 80 1C 0C 80 45 0D 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0080: 66 64 69 31 0B 80 5B 0E  80 22 90 11 01 22 90 11  fdi1..[.."..."..
0090: 01 74 6C 6B 30 2B 22 90  11 01 0F 80 23 2B 22 90  .tlk0+".....#+".
00A0: 11 01 10 80 23 1A BC 03  1C 09 80 52 0A 80 F0 FF  ....#......R....
00B0: FF 7F F0 FF FF 7F 73 30  30 30 1C 0C 80 AB 11 0B  ......s000......
00C0: 80 1C 11 80 AB 0A 46 00  45 0D 80 F0 FF FF 7F F0  ......F.E.......
00D0: FF FF 7F 66 64 69 32 0B  80 21 00                 ...fdi2..!.     
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1A] CALL_SUBROUTINE(address=0x03BC)
  2: 0x0005 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0007 [0x38] SET_CLIENT_EVENT_MODE(mode=147*)
  4: 0x000A [0x2F] Morimar (ID: 17928226/0x01119022)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x0010 [0x4E] SET_ENTITY_HIDE_FLAG: Show Morimar (ID: 17928226/0x01119022)
  6: 0x0016 [0x92] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  7: 0x001C [0x94] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  8: 0x0022 [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  9: 0x0028 [0xBA] SET_ENTITY_POSITION(entity_id=Morimar (ID: 17928226/0x01119022), pos_x=-19.381*, pos_z=17.465*, pos_y=-0.403*, direction=249.6°*)
 10: 0x0035 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-19.010*, pos_z=20.927*, pos_y=-0.563*, direction=44.6°*)
 11: 0x0042 [0x80] LOAD_WAIT(entity=Morimar (ID: 17928226/0x01119022))
 12: 0x0047 [0x80] LOAD_WAIT(entity=LocalPlayer)
 13: 0x004C [0x4A] Morimar (ID: 17928226/0x01119022) looks at LocalPlayer
 14: 0x0055 [0x4A] LocalPlayer looks at Morimar (ID: 17928226/0x01119022)
 15: 0x005E [0x1C] WAIT(30* ticks)
 16: 0x0061 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=[631*, 0*]
 17: 0x0072 [0x1C] WAIT(15* ticks)
 18: 0x0075 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0086 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Morimar (ID: 17928226/0x01119022), Morimar (ID: 17928226/0x01119022)], work=3476*
 20: 0x0095 [0x2B] Morimar (ID: 17928226/0x01119022) [7408*]:
    → "I know you're itchin' to get started, but we've got to wait for Darrcuiln to bring your princess."
 21: 0x009C [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x009D [0x2B] Morimar (ID: 17928226/0x01119022) [7409*]:
    → "How's 'bout takin' a look around while ya wait?"
 23: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00A5 [0x1A] CALL_SUBROUTINE(address=0x03BC)
 25: 0x00A8 [0x1C] WAIT(30* ticks)
 26: 0x00AB [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=631*
 27: 0x00BA [0x1C] WAIT(15* ticks)
 28: 0x00BD [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
 29: 0x00C1 [0x1C] WAIT(1* ticks)
 30: 0x00C4 [0xAB] EventEntity->UnknownFlag = 0 // Disable unknown flag
 31: 0x00C6 [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x00C8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 33: 0x00D9 [0x21] END_EVENT
 34: 0x00DA [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DB    |
| Data Size    | 210 bytes |
| Instructions | 33        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   42 1A BC 03 46             B...F
00E0: 01 38 00 80 2F 00 22 90  11 01 4E 00 22 90 11 01  .8../."...N."...
00F0: 92 01 22 90 11 01 94 01  22 90 11 01 94 01 F0 FF  ..".....".......
0100: FF 7F BA 22 90 11 01 01  80 02 80 03 80 04 80 BA  ..."............
0110: F0 FF FF 7F 05 80 06 80  07 80 08 80 80 22 90 11  ............."..
0120: 01 80 F0 FF FF 7F 4A 22  90 11 01 F0 FF FF 7F 4A  ......J".......J
0130: F0 FF FF 7F 22 90 11 01  1C 09 80 45 0A 80 F0 FF  ...."......E....
0140: FF 7F F0 FF FF 7F 73 30  30 30 0B 80 1C 0C 80 45  ......s000.....E
0150: 0D 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 0B 80  ..........fdi1..
0160: 5B 0E 80 22 90 11 01 22  90 11 01 74 6C 6B 30 2B  [.."..."...tlk0+
0170: 22 90 11 01 12 80 23 1A  BC 03 1C 09 80 52 0A 80  ".....#......R..
0180: F0 FF FF 7F F0 FF FF 7F  73 30 30 30 1C 0C 80 AB  ........s000....
0190: 11 0B 80 1C 11 80 AB 0A  46 00 45 0D 80 F0 FF FF  ........F.E.....
01A0: 7F F0 FF FF 7F 66 64 69  32 0B 80 21 00           .....fdi2..!.   
```

#### Opcodes

```
  0: 0x00DB [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00DC [0x1A] CALL_SUBROUTINE(address=0x03BC)
  2: 0x00DF [0x46] CAMERA_CONTROL: Disable user control
  3: 0x00E1 [0x38] SET_CLIENT_EVENT_MODE(mode=147*)
  4: 0x00E4 [0x2F] Morimar (ID: 17928226/0x01119022)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x00EA [0x4E] SET_ENTITY_HIDE_FLAG: Show Morimar (ID: 17928226/0x01119022)
  6: 0x00F0 [0x92] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  7: 0x00F6 [0x94] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  8: 0x00FC [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  9: 0x0102 [0xBA] SET_ENTITY_POSITION(entity_id=Morimar (ID: 17928226/0x01119022), pos_x=-19.381*, pos_z=17.465*, pos_y=-0.403*, direction=249.6°*)
 10: 0x010F [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-19.010*, pos_z=20.927*, pos_y=-0.563*, direction=44.6°*)
 11: 0x011C [0x80] LOAD_WAIT(entity=Morimar (ID: 17928226/0x01119022))
 12: 0x0121 [0x80] LOAD_WAIT(entity=LocalPlayer)
 13: 0x0126 [0x4A] Morimar (ID: 17928226/0x01119022) looks at LocalPlayer
 14: 0x012F [0x4A] LocalPlayer looks at Morimar (ID: 17928226/0x01119022)
 15: 0x0138 [0x1C] WAIT(30* ticks)
 16: 0x013B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=[631*, 0*]
 17: 0x014C [0x1C] WAIT(15* ticks)
 18: 0x014F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0160 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Morimar (ID: 17928226/0x01119022), Morimar (ID: 17928226/0x01119022)], work=3476*
 20: 0x016F [0x2B] Morimar (ID: 17928226/0x01119022) [7546*]:
    → "I'll handle the cleanup. Ya gotta go back to Adoulin with Arciela."
 21: 0x0176 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0177 [0x1A] CALL_SUBROUTINE(address=0x03BC)
 23: 0x017A [0x1C] WAIT(30* ticks)
 24: 0x017D [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=631*
 25: 0x018C [0x1C] WAIT(15* ticks)
 26: 0x018F [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
 27: 0x0193 [0x1C] WAIT(1* ticks)
 28: 0x0196 [0xAB] EventEntity->UnknownFlag = 0 // Disable unknown flag
 29: 0x0198 [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x019A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x01AB [0x21] END_EVENT
 32: 0x01AC [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01AD    |
| Data Size    | 218 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                         42 1A BC               B..
01B0: 03 46 01 38 00 80 2F 00  22 90 11 01 4E 00 22 90  .F.8../."...N.".
01C0: 11 01 92 01 22 90 11 01  94 01 22 90 11 01 94 01  ....".....".....
01D0: F0 FF FF 7F BA 22 90 11  01 01 80 02 80 03 80 04  ....."..........
01E0: 80 BA F0 FF FF 7F 05 80  06 80 07 80 08 80 80 22  ..............."
01F0: 90 11 01 80 F0 FF FF 7F  4A 22 90 11 01 F0 FF FF  ........J"......
0200: 7F 4A F0 FF FF 7F 22 90  11 01 1C 09 80 45 0A 80  .J...."......E..
0210: F0 FF FF 7F F0 FF FF 7F  73 30 30 30 0B 80 1C 0C  ........s000....
0220: 80 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0230: 0B 80 5B 0E 80 22 90 11  01 22 90 11 01 74 6C 6B  ..[.."..."...tlk
0240: 30 2B 22 90 11 01 13 80  23 2B 22 90 11 01 14 80  0+".....#+".....
0250: 23 1A BC 03 1C 09 80 52  0A 80 F0 FF FF 7F F0 FF  #......R........
0260: FF 7F 73 30 30 30 1C 0C  80 AB 11 0B 80 1C 11 80  ..s000..........
0270: AB 0A 46 00 45 0D 80 F0  FF FF 7F F0 FF FF 7F 66  ..F.E..........f
0280: 64 69 32 0B 80 21 00                              di2..!.         
```

#### Opcodes

```
  0: 0x01AD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01AE [0x1A] CALL_SUBROUTINE(address=0x03BC)
  2: 0x01B1 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x01B3 [0x38] SET_CLIENT_EVENT_MODE(mode=147*)
  4: 0x01B6 [0x2F] Morimar (ID: 17928226/0x01119022)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x01BC [0x4E] SET_ENTITY_HIDE_FLAG: Show Morimar (ID: 17928226/0x01119022)
  6: 0x01C2 [0x92] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  7: 0x01C8 [0x94] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  8: 0x01CE [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  9: 0x01D4 [0xBA] SET_ENTITY_POSITION(entity_id=Morimar (ID: 17928226/0x01119022), pos_x=-19.381*, pos_z=17.465*, pos_y=-0.403*, direction=249.6°*)
 10: 0x01E1 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-19.010*, pos_z=20.927*, pos_y=-0.563*, direction=44.6°*)
 11: 0x01EE [0x80] LOAD_WAIT(entity=Morimar (ID: 17928226/0x01119022))
 12: 0x01F3 [0x80] LOAD_WAIT(entity=LocalPlayer)
 13: 0x01F8 [0x4A] Morimar (ID: 17928226/0x01119022) looks at LocalPlayer
 14: 0x0201 [0x4A] LocalPlayer looks at Morimar (ID: 17928226/0x01119022)
 15: 0x020A [0x1C] WAIT(30* ticks)
 16: 0x020D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=[631*, 0*]
 17: 0x021E [0x1C] WAIT(15* ticks)
 18: 0x0221 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0232 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Morimar (ID: 17928226/0x01119022), Morimar (ID: 17928226/0x01119022)], work=3476*
 20: 0x0241 [0x2B] Morimar (ID: 17928226/0x01119022) [7547*]:
    → "What're ya doin' back here? I don't recall puttin' out a signal."
 21: 0x0248 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0249 [0x2B] Morimar (ID: 17928226/0x01119022) [7548*]:
    → "Ya've already spread the news, right? Then it's only a matter of time before they find the body."
 23: 0x0250 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0251 [0x1A] CALL_SUBROUTINE(address=0x03BC)
 25: 0x0254 [0x1C] WAIT(30* ticks)
 26: 0x0257 [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=631*
 27: 0x0266 [0x1C] WAIT(15* ticks)
 28: 0x0269 [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
 29: 0x026D [0x1C] WAIT(1* ticks)
 30: 0x0270 [0xAB] EventEntity->UnknownFlag = 0 // Disable unknown flag
 31: 0x0272 [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x0274 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 33: 0x0285 [0x21] END_EVENT
 34: 0x0286 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0287    |
| Data Size    | 867 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0280:                      42  1A BC 03 46 01 38 00 80         B...F.8..
0290: 2F 00 22 90 11 01 4E 00  22 90 11 01 92 01 22 90  /."...N.".....".
02A0: 11 01 94 01 22 90 11 01  94 01 F0 FF FF 7F BA 22  ....".........."
02B0: 90 11 01 01 80 02 80 03  80 04 80 BA F0 FF FF 7F  ................
02C0: 05 80 06 80 07 80 08 80  80 22 90 11 01 80 F0 FF  ........."......
02D0: FF 7F 4A 22 90 11 01 F0  FF FF 7F 4A F0 FF FF 7F  ..J".......J....
02E0: 22 90 11 01 1C 09 80 45  0A 80 F0 FF FF 7F F0 FF  "......E........
02F0: FF 7F 73 30 30 30 0B 80  1C 0C 80 45 0D 80 F0 FF  ..s000.....E....
0300: FF 7F F0 FF FF 7F 66 64  69 31 0B 80 5B 0E 80 22  ......fdi1..[.."
0310: 90 11 01 22 90 11 01 74  6C 6B 30 2B 22 90 11 01  ..."...tlk0+"...
0320: 15 80 23 1A BC 03 1C 09  80 52 0A 80 F0 FF FF 7F  ..#......R......
0330: F0 FF FF 7F 73 30 30 30  1C 0C 80 AB 11 0B 80 1C  ....s000........
0340: 11 80 AB 0A 46 00 45 0D  80 F0 FF FF 7F F0 FF FF  ....F.E.........
0350: 7F 66 64 69 32 0B 80 21  00 45 0D 80 F0 FF FF 7F  .fdi2..!.E......
0360: F0 FF FF 7F 66 64 69 30  0B 80 55 0D 80 F0 FF FF  ....fdi0..U.....
0370: 7F F0 FF FF 7F 66 64 69  30 1B 45 0D 80 F0 FF FF  .....fdi0.E.....
0380: 7F F0 FF FF 7F 66 64 6F  30 0B 80 55 0D 80 F0 FF  .....fdo0..U....
0390: FF 7F F0 FF FF 7F 66 64  6F 30 1B 45 0D 80 F0 FF  ......fdo0.E....
03A0: FF 7F F0 FF FF 7F 66 64  69 31 0B 80 55 0D 80 F0  ......fdi1..U...
03B0: FF FF 7F F0 FF FF 7F 66  64 69 31 1B 45 0D 80 F0  .......fdi1.E...
03C0: FF FF 7F F0 FF FF 7F 66  64 6F 31 0B 80 55 0D 80  .......fdo1..U..
03D0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 1B 45 16 80  ........fdo1.E..
03E0: F0 FF FF 7F F0 FF FF 7F  77 68 69 31 0B 80 55 16  ........whi1..U.
03F0: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 31 1B 45 16  .........whi1.E.
0400: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 31 0B 80 55  .........who1..U
0410: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 31 1B 45  ..........who1.E
0420: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 32 0B 80  ..........who2..
0430: 55 16 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 32 1B  U..........who2.
0440: 45 16 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 33 0B  E..........who3.
0450: 80 55 16 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 33  .U..........who3
0460: 1B 62 11 80 F0 FF FF 7F  F0 FF FF 7F 6D 61 69 6E  .b..........main
0470: 0B 80 1C 17 80 45 0D 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0480: 66 64 6F 31 0B 80 55 0D  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
0490: 7F 66 64 6F 31 1B 45 0D  80 F0 FF FF 7F F0 FF FF  .fdo1.E.........
04A0: 7F 66 64 69 31 0B 80 62  18 80 F0 FF FF 7F F0 FF  .fdi1..b........
04B0: FF 7F 6D 61 69 6E 0B 80  1C 09 80 55 0D 80 F0 FF  ..main.....U....
04C0: FF 7F F0 FF FF 7F 66 64  69 31 1B 45 0D 80 F0 FF  ......fdi1.E....
04D0: FF 7F F0 FF FF 7F 62 6C  6F 6E 0B 80 45 16 80 F0  ......blon..E...
04E0: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 0B 80 1B 45 16  .......blon...E.
04F0: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 30 0B 80 55  .........whi0..U
0500: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 69 30 1B 45  ..........whi0.E
0510: 16 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 30 0B 80  ..........who0..
0520: 55 16 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 30 1B  U..........who0.
0530: 45 19 80 F0 FF FF 7F F0  FF FF 7F 65 66 6F 6E 0B  E..........efon.
0540: 80 55 19 80 F0 FF FF 7F  F0 FF FF 7F 65 66 6F 6E  .U..........efon
0550: 1B 45 0D 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 73  .E..........fdis
0560: 0B 80 1B 45 0D 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0570: 6F 73 0B 80 55 0D 80 F0  FF FF 7F F0 FF FF 7F 66  os..U..........f
0580: 64 6F 73 1B 45 0D 80 F0  FF FF 7F F0 FF FF 7F 66  dos.E..........f
0590: 64 69 66 0B 80 1B 45 0D  80 F0 FF FF 7F F0 FF FF  dif...E.........
05A0: 7F 66 64 6F 66 0B 80 55  0D 80 F0 FF FF 7F F0 FF  .fdof..U........
05B0: FF 7F 66 64 6F 66 1B 45  0D 80 F0 FF FF 7F F0 FF  ..fdof.E........
05C0: FF 7F 66 64 69 70 0B 80  1B 45 0D 80 F0 FF FF 7F  ..fdip...E......
05D0: F0 FF FF 7F 66 64 6F 70  0B 80 55 0D 80 F0 FF FF  ....fdop..U.....
05E0: 7F F0 FF FF 7F 66 64 6F  70 1B                    .....fdop.      
```

#### Opcodes

```
  0: 0x0287 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0288 [0x1A] CALL_SUBROUTINE(address=0x03BC)
  2: 0x028B [0x46] CAMERA_CONTROL: Disable user control
  3: 0x028D [0x38] SET_CLIENT_EVENT_MODE(mode=147*)
  4: 0x0290 [0x2F] Morimar (ID: 17928226/0x01119022)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x0296 [0x4E] SET_ENTITY_HIDE_FLAG: Show Morimar (ID: 17928226/0x01119022)
  6: 0x029C [0x92] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  7: 0x02A2 [0x94] Morimar (ID: 17928226/0x01119022)->Render.Flags3 ^= 0x01
  8: 0x02A8 [0x94] LocalPlayer->Render.Flags3 ^= 0x01
  9: 0x02AE [0xBA] SET_ENTITY_POSITION(entity_id=Morimar (ID: 17928226/0x01119022), pos_x=-19.381*, pos_z=17.465*, pos_y=-0.403*, direction=249.6°*)
 10: 0x02BB [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-19.010*, pos_z=20.927*, pos_y=-0.563*, direction=44.6°*)
 11: 0x02C8 [0x80] LOAD_WAIT(entity=Morimar (ID: 17928226/0x01119022))
 12: 0x02CD [0x80] LOAD_WAIT(entity=LocalPlayer)
 13: 0x02D2 [0x4A] Morimar (ID: 17928226/0x01119022) looks at LocalPlayer
 14: 0x02DB [0x4A] LocalPlayer looks at Morimar (ID: 17928226/0x01119022)
 15: 0x02E4 [0x1C] WAIT(30* ticks)
 16: 0x02E7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=[631*, 0*]
 17: 0x02F8 [0x1C] WAIT(15* ticks)
 18: 0x02FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x030C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Morimar (ID: 17928226/0x01119022), Morimar (ID: 17928226/0x01119022)], work=3476*
 20: 0x031B [0x2B] Morimar (ID: 17928226/0x01119022) [7549*]:
    → "The princess'll need yer help now more than ever. Make sure she stays on the right path--for Adoulin's sake."
 21: 0x0322 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0323 [0x1A] CALL_SUBROUTINE(address=0x03BC)
 23: 0x0326 [0x1C] WAIT(30* ticks)
 24: 0x0329 [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=631*
 25: 0x0338 [0x1C] WAIT(15* ticks)
 26: 0x033B [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
 27: 0x033F [0x1C] WAIT(1* ticks)
 28: 0x0342 [0xAB] EventEntity->UnknownFlag = 0 // Disable unknown flag
 29: 0x0344 [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x0346 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x0357 [0x21] END_EVENT
 32: 0x0358 [0x00] END_REQSTACK()

SUBROUTINE_03BC:
 33: 0x03BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 34: 0x03CD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 35: 0x03DC [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0359 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x036A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0379 [0x1B] RETURN
     0x037A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x038B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x039A [0x1B] RETURN
     0x039B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03AC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03BB [0x1B] RETURN
# Dead code (unreachable instructions):
     0x03DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x03EE [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x03FD [0x1B] RETURN
     0x03FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x040F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x041E [0x1B] RETURN
     0x041F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0430 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x043F [0x1B] RETURN
     0x0440 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0451 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0460 [0x1B] RETURN
     0x0461 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x0472 [0x1C] WAIT(45* ticks)
     0x0475 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0486 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0495 [0x1B] RETURN
     0x0496 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x04A7 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x04B8 [0x1C] WAIT(30* ticks)
     0x04BB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x04CA [0x1B] RETURN
     0x04CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x04DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x04ED [0x1B] RETURN
     0x04EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x04FF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x050E [0x1B] RETURN
     0x050F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0520 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x052F [0x1B] RETURN
     0x0530 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x0541 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0550 [0x1B] RETURN
     0x0551 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0562 [0x1B] RETURN
     0x0563 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0574 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0583 [0x1B] RETURN
     0x0584 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0595 [0x1B] RETURN
     0x0596 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x05A7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x05B6 [0x1B] RETURN
     0x05B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x05C8 [0x1B] RETURN
     0x05C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x05DA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x05E9 [0x1B] RETURN
```
